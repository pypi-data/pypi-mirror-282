# PyMailScraper

PyMailScraper is a powerful and easy-to-use Python tool for scraping email addresses from websites. It can crawl multiple pages, respect throttling limits, and save results in a convenient CSV format.

## Installation

You can install PyMailScraper using pip:

```sh
pip install pymailscraper
```

## Usage

PyMailScraper can be used both as a command-line tool and as a Python library.

### Command-line Usage

After installation, you can use PyMailScraper from the command line:

```sh
pymailscraper [OPTIONS]
```

#### Options:

- `-u`, `--urls`: One or more URLs to scrape. You can provide multiple URLs separated by spaces.
  Example: `pymailscraper -u https://example.com https://another-example.com`

- `-f`, `--file`: Path to a file containing URLs (one per line).
  Example: `pymailscraper -f urls.txt`

- `-o`, `--output`: Output CSV file path (default: "email_results.csv").
  Example: `pymailscraper -u https://example.com -o my_results.csv`

- `-d`, `--depth`: Maximum depth to crawl (default: 3).
  Example: `pymailscraper -u https://example.com -d 5`

- `-p`, `--pages`: Maximum number of pages to crawl per website (default: 100).
  Example: `pymailscraper -u https://example.com -p 50`

- `--common-pages-only`: Crawl only common pages (default: False).
  Example: `pymailscraper -u https://example.com --common-pages-only`

- `--use-common-pages`: Use common pages in crawling (default: False).
  Example: `pymailscraper -u https://example.com --use-common-pages`

- `--throttle`: Delay between requests in seconds (default: 0).
  Example: `pymailscraper -u https://example.com --throttle 1.5`

- `--auto-throttle`: Automatically adjust throttle on 'Too many requests' responses.
  Example: `pymailscraper -u https://example.com --auto-throttle`

- `--max-throttle`: Maximum throttle delay in seconds (default: 5).
  Example: `pymailscraper -u https://example.com --auto-throttle --max-throttle 10`

### Python Library Usage

You can also use PyMailScraper in your Python scripts:

```python
from pymailscraper import EmailScraper

scraper = EmailScraper(
    output_file="results.csv",
    max_depth=3,
    max_pages=100,
    throttle=1.0,
    auto_throttle=True
)

urls = ["https://example.com", "https://another-example.com"]
scraper.run(urls)
```

## Examples

1. Scrape a single website:

```sh
pymailscraper -u https://example.com
```

2. Scrape multiple websites:

```sh
pymailscraper -u https://example.com https://another-example.com
```

3. Scrape websites from a file with custom output and depth:

```sh
pymailscraper -f urls.txt -o results.csv -d 5
```

4. Use auto-throttling with a maximum of 50 pages per site:

```sh
pymailscraper -u https://example.com --auto-throttle -p 50
```

## Output

PyMailScraper saves the results in a CSV file with the following columns:

- URL: The page where the email was found
- Email: The email address
- Name: Any associated name found (if available)

## Ethical Usage

Please use this tool responsibly. Always respect the website's terms of service, robots.txt files, and any legal restrictions on scraping. Be mindful of the load you're putting on websites and use throttling when appropriate.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.

## Support
If you encounter any problems or have any questions, please open an issue on the GitHub repository.

Happy scraping!