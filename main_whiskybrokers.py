from utils.request_util import get_response_from_url
from utils.html_parser_util import Parser
from utils.config_parser import Parameters

first_page = get_response_from_url(Parameters.whiskybroker_base_url)
first_page_parser = Parser(content=first_page.content)


all_whiskies = []
first_whiskies = first_page_parser.get_whiskies_information()
all_whiskies.append(first_whiskies)

extra_pages_amount = first_page_parser.get_extra_pages_amount()
for i in range(0, extra_pages_amount):
    #build new page url
    #add +2, once for indexing from 1 and once because we already scraped the first page
    url = Parameters.whiskybroker_base_url + f'page={i+2}'
    page = get_response_from_url(url=url)
    page_parser = Parser(content=page.content)
    page_whiskies = page_parser.get_whiskies_information()
    all_whiskies.append(page_whiskies)

all_whiskies = [whisky for whisky_list in all_whiskies for whisky in whisky_list]
print(all_whiskies)
print(len(all_whiskies))

