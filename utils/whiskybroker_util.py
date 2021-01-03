from utils.request_util import get_response_from_url
from utils.html_parser_util import Parser

class whiskybroker_scraper:
    def __init__(self, base_url):
        self.base_url = base_url


    def get_page_content(self, url):
        return get_response_from_url(url)

    def scrape_page(self, url):
        parser = Parser(content=self.get_page_content(url))
        return parser.get_whiskies_information()

    # scrape both whiskies and amount of pages that we will need to scrape
    def scrape_first_page(self):
        parser = Parser(content=self.get_page_content(self.base_url))
        whiskies = parser.get_whiskies_information()
        extra_page_amount = parser.get_extra_pages_amount()
        return whiskies, extra_page_amount

    # main function to use
    def scrape_all_pages(self):
        all_whiskies = []
        first_whiskies, extra_pages_amount_to_scrape = self.scrape_first_page()
        for i in range(0, extra_pages_amount_to_scrape):
            #add 2 to i, once to offset indexing from 1, and once because we already scraped the first page
            url = self.base_url + f'page={i+2}'
            page = get_response_from_url(url)
            page_parser = Parser(content=page.content)
            page_whiskies = page_parser.get_whiskies_information()
            all_whiskies.append(page_whiskies)
        #flatten sublists
        all_whiskies = [whisky for whisky_list in all_whiskies for whisky in whisky_list]
        return all_whiskies





