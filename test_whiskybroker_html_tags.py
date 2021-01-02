import requests
from bs4 import BeautifulSoup

#parses the amounts from the string sentence
def get_amounts_from_string(string_amounts):
    amounts_list = []
    amount_str = ''
    for character in amounts:
        print(character)
        if character.isdigit():
            amount_str += character
        else:
            if amount_str != '':
                amounts_list.append(amount_str)
            amount_str = ''
    return amounts_list

#gets the amount of pages that we need to scrape for whiskyies
def get_amount_of_pages_from_amouns(amounts):
    return (amounts[2] // amounts[1]) + 1


DEFAULT_HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
url = 'https://www.whiskybroker.co.uk/bottles-c-1'
page_extension = '-page-' #-page-X

page = requests.get(url, headers = DEFAULT_HEADERS)
parser = BeautifulSoup(page.content, 'html.parser')

get_amount_of_items = parser.find('span', class_='input-group-addon')
amounts = get_amount_of_items.get_text()


#div id that contains bottle names: col-xs-12 col-sm-10
whiskies = parser.find_all('div', class_='col-xs-12 col-sm-10')


for whisky in whiskies:
    description = whisky.find('p', class_='shortdesc')
    price = whisky.find('span', class_='price')
    orderable = whisky.find('div', class_='button-box')
    if orderable is None:
        print('you can not order this whisky yet :(')
    else:
        print('whisky is for sale, cheers!')