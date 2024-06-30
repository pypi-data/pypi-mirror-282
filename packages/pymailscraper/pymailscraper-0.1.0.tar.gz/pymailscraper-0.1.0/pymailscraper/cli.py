import argparse
import os
from .scraper import EmailScraper

def main():
    parser = argparse.ArgumentParser(description="Email scraper script")
    parser.add_argument("-u", "--urls", nargs="+", help="One or more URLs to scrape")
    parser.add_argument("-f", "--file", help="Path to a file containing URLs (one per line)")
    parser.add_argument("-o", "--output", default="email_results.csv", help="Output CSV file path")
    parser.add_argument("-d", "--depth", type=int, default=3, help="Maximum depth to crawl (default: 3)")
    parser.add_argument("-p", "--pages", type=int, default=100, help="Maximum number of pages to crawl per website (default: 100)")
    parser.add_argument("--common-pages-only", action="store_true", help="Crawl only common pages (default: False)")
    parser.add_argument("--use-common-pages", action="store_true", help="Use common pages in crawling (default: False)")
    parser.add_argument("--common-pages", nargs="+", help="Specify additional common pages to crawl")
    parser.add_argument("--common-pages-file", help="Path to a file containing common pages (one per line)")
    parser.add_argument("--throttle", type=float, default=0, help="Delay between requests in seconds (default: 0)")
    parser.add_argument("--auto-throttle", action="store_true", help="Automatically adjust throttle on 'Too many requests' responses")
    parser.add_argument("--max-throttle", type=float, default=5, help="Maximum throttle delay in seconds (default: 5)")

    
    args = parser.parse_args()

    urls = []
    if args.urls:
        urls.extend(args.urls)
    if args.file:
        if os.path.exists(args.file):
            urls.extend(EmailScraper(args.output).read_urls_from_file(args.file))
        else:
            print(f"Input file not found: {args.file}")
            return

    # If no URLs provided, use a default file
    if not urls:
        default_url_file = "urls.txt"
        if os.path.exists(default_url_file):
            urls.extend(EmailScraper(args.output).read_urls_from_file(default_url_file))
            print(f"Using URLs from default file: {default_url_file}")
        else:
            print(f"No URLs provided and default file '{default_url_file}' not found.")
            parser.print_help()
            return
    
    scraper = EmailScraper(args.output, max_depth=args.depth, max_pages=args.pages, 
                           common_pages_only=args.common_pages_only, 
                           use_common_pages=args.use_common_pages or args.common_pages_only,
                           throttle=args.throttle, auto_throttle=args.auto_throttle,
                           max_throttle=args.max_throttle)
    
    if args.common_pages:
        scraper.common_pages.extend(args.common_pages)
    
    if args.common_pages_file:
        if os.path.exists(args.common_pages_file):
            additional_common_pages = scraper.read_common_pages_from_file(args.common_pages_file)
            scraper.common_pages.extend(additional_common_pages)
            print(f"Added common pages from file: {args.common_pages_file}")
        else:
            print(f"Common pages file not found: {args.common_pages_file}")

    scraper.run(urls)

if __name__ == "__main__":
    main()
