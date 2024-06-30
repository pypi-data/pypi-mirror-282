import unittest
from unittest.mock import patch, MagicMock
from pymailscraper.scraper import EmailScraper

class TestEmailScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = EmailScraper('test_output.csv')

    def test_init(self):
        self.assertEqual(self.scraper.output_file, 'test_output.csv')
        self.assertEqual(self.scraper.max_depth, 3)
        self.assertEqual(self.scraper.max_pages, 100)

    @patch('pymailscraper.scraper.requests.get')
    def test_get_page_content(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '<html><body>Test content</body></html>'
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        content = self.scraper.get_page_content('http://example.com')
        self.assertEqual(content, '<html><body>Test content</body></html>')

    def test_extract_emails(self):
        content = 'Contact us at test@example.com or support@example.com'
        emails = self.scraper.extract_emails(content)
        self.assertEqual(set(emails), {'test@example.com', 'support@example.com'})

if __name__ == '__main__':
    unittest.main()
