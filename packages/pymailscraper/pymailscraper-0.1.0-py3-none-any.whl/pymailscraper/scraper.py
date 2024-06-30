import csv
import re
import requests
from bs4 import BeautifulSoup
import traceback
from requests.exceptions import RequestException, TooManyRedirects
from urllib.parse import urljoin, urlparse, urldefrag
from tqdm import tqdm
import time

class EmailScraper:
    def __init__(self, output_file, max_depth=3, max_pages=100, common_pages_only=False, use_common_pages=True, 
                 throttle=0, auto_throttle=False, max_throttle=5):
        self.output_file = output_file
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.common_pages_only = common_pages_only
        self.use_common_pages = use_common_pages
        self.initial_throttle = throttle
        self.current_throttle = 0
        self.auto_throttle = auto_throttle
        self.max_throttle = max_throttle
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.email_set = set()
        self.visited_urls = set()
        self.common_pages = [
            '/about', '/about-us', '/aboutus',
            '/contact', '/contact-us', '/contactus',
            '/team', '/our-team', '/ourteam',
            '/staff', '/our-staff', '/ourstaff',
            '/people', '/our-people', '/ourpeople',
            '/info', '/information',
            '/support'
        ]

        self.visited_urls = set()
        self.visited_base_urls = set()
        self.visited_anchors = set()

    def read_urls_from_file(self, input_file):
        try:
            with open(input_file, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except IOError as e:
            print(f"Error reading input file: {e}")
            return []

    def get_page_content(self, url):
        try:
            if self.current_throttle > 0:
                time.sleep(self.current_throttle)
            
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code == 429 and self.auto_throttle:
                if self.current_throttle >= self.max_throttle:
                    return None
                self.current_throttle = min(self.current_throttle + self.initial_throttle, self.max_throttle)
                time.sleep(5)
                return self.get_page_content(url)
            
            response.raise_for_status()
            return response.text
        except RequestException as e:
            if isinstance(e, TooManyRedirects) and self.auto_throttle:
                if self.current_throttle >= self.max_throttle:
                    return None
                self.current_throttle = min(self.current_throttle + self.initial_throttle, self.max_throttle)
            return None

    def extract_emails(self, content):
        if not content:
            return []
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, content)

    def extract_name(self, soup):
        try:
            if soup is None:
                return None
            name_tags = soup.find_all(['h1', 'h2', 'h3', 'strong'], string=re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'))
            if name_tags:
                return name_tags[0].text.strip()
        except Exception as e:
            print(f"Error extracting name: {e}")
        return None

    def get_internal_links(self, url, soup):
        internal_links = set()
        base_url = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))
        
        if soup is None:
            return internal_links

        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)
            if full_url.startswith(base_url) and full_url not in self.visited_urls:
                internal_links.add(full_url)
        
        return internal_links
    
    def get_common_page_urls(self, base_url):
        return [urljoin(base_url, page) for page in self.common_pages]
    
    def read_common_pages_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except IOError as e:
            print(f"Error reading common pages file: {e}")
            return []

    def crawl_website(self, start_url):
        self.current_throttle = self.initial_throttle
        queue = [(start_url, 0)]
        results = []
        pages_crawled = 0

        with tqdm(desc=f"Crawling {start_url}", unit="page") as pbar:
            while queue and pages_crawled < self.max_pages:
                url, depth = queue.pop(0)
                normalized_url = self.normalize_url(url)
                
                if not self.should_crawl(normalized_url):
                    continue

                if depth > self.max_depth:
                    continue

                base, anchor = urldefrag(normalized_url)
                self.visited_base_urls.add(base)
                if anchor:
                    self.visited_anchors.add((base, anchor))

                pages_crawled += 1
                pbar.set_description(f"Crawling {normalized_url}")

                content = self.get_page_content(normalized_url)
                
                if content:
                    try:
                        soup = BeautifulSoup(content, 'html.parser')
                        emails = self.extract_emails(content)
                        name = self.extract_name(soup)

                        for email in emails:
                            if email not in self.email_set:
                                self.email_set.add(email)
                                results.append({
                                    'url': normalized_url,
                                    'email': email,
                                    'name': name if name else 'N/A'
                                })

                        if depth < self.max_depth:
                            internal_links = self.get_internal_links(normalized_url, soup)
                            new_links = [(link, depth + 1) for link in internal_links if self.should_crawl(link)]
                            queue.extend(new_links)
                    except Exception as e:
                        print(f"Error parsing content: {e}")
                        traceback.print_exc()

                pbar.update(1)

        return results
    
    def normalize_url(self, url):
        base, anchor = urldefrag(url)
        normalized = base.rstrip('/')
        if anchor:
            normalized += f'#{anchor}'
        return normalized

    def should_crawl(self, url):
        base, anchor = urldefrag(url)
        if base not in self.visited_base_urls:
            return True
        if anchor and (base, anchor) not in self.visited_anchors:
            # You might want to implement a cooldown period here
            return True
        return False

    def scrape_emails(self, urls):
        all_results = []
        for url in urls:
            if not url.startswith('http'):
                url = 'http://' + url
            print(f"\nScraping website: {url}")
            results = self.crawl_website(url)
            all_results.extend(results)
            self.visited_urls.clear()  # Clear visited URLs for the next website
        return all_results

    def save_results(self, results):
        try:
            with open(self.output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['url', 'email', 'name'])
                writer.writeheader()
                writer.writerows(results)
        except IOError as e:
            print(f"Error writing to CSV file: {e}")
            print("Attempting to save results to a backup file...")
            self.save_results_backup(results)

    def save_results_backup(self, results):
        backup_file = f"backup_{self.output_file}"
        try:
            with open(backup_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['url', 'email', 'name'])
                writer.writeheader()
                writer.writerows(results)
            print(f"Results saved to backup file: {backup_file}")
        except IOError as e:
            print(f"Error writing to backup file: {e}")
            print("Unable to save results. Here are the found emails:")
            for result in results:
                print(f"URL: {result['url']}, Email: {result['email']}, Name: {result['name']}")

    def run(self, urls):
        all_results = []
        for url in urls:
            if not url.startswith('http'):
                url = 'http://' + url
            results = self.crawl_website(url)
            all_results.extend(results)
            self.visited_urls.clear()
        self.save_results(all_results)
