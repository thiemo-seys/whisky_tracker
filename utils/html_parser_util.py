from bs4 import BeautifulSoup

#TODO: this needs a lot of error checking and input validation etc...

class Parser:
    def __init__(self, content, parser='html.parser'):
        self.content = content
        self.parser = self.create_parser(content, parser)


    def create_parser(self, html_content, parser='html.parser'):
        return BeautifulSoup(html_content, parser)

    def pretty_print(self):
        print(self.parser.prettify())

    def get_children(self):
        return self.parser.children

    #normaly returns a generator, but we cast it to a list to use it more easily(we don't have to worry about the performance difference for the small amount of parsing we are doing)
    def get_children_as_list(self):
        return list(self.get_children())


    def select_tag_by_index(self, children ,index):
        return children[index]

    def get_tag_text(self, tag):
        return tag.get_text()

#==========================================================================================================================================
    #TODO: rename these functions, this is an utter mess!

    #get the string containg the information about the page/whisky amounts
    def get_amount_information(self):
        return self.parser.find('span', class_='input-group-addon').get_text()

    # parses the amounts from the string sentence
    def get_amounts_from_string(self, string_amounts):
        amounts_list = []
        amount_str = ''
        for character in string_amounts:
            if character.isdigit():
                amount_str += character
            else:
                if amount_str != '':
                    amounts_list.append(amount_str)
                amount_str = ''
        return amounts_list

    # gets the amount of pages that we need to scrape for whiskyies
    def get_amount_of_pages_from_amounts(self, amounts):
        return (int(amounts[2]) // int(amounts[1]))


    def get_extra_pages_amount(self):
        html_info = self.get_amount_information()
        whiskies_amounts = self.get_amounts_from_string(html_info)
        extra_page_amount = self.get_amount_of_pages_from_amounts(whiskies_amounts)
        return extra_page_amount

    #Specific whisky utilities
    def get_whisky_attribute(self, whisky, attribute):
        possible_attributes = ['description', 'price', 'orderable']
        if attribute not in possible_attributes:
            raise NotImplementedError(f'{attribute} is not yet implemented, only: {possible_attributes} are implemented')

        if attribute == possible_attributes[0]:
            whisky_attribute =  self.get_whisky_description(whisky)
        elif attribute == possible_attributes[1]:
            whisky_attribute = self.get_whisky_price(whisky)
        elif attribute == possible_attributes[2]:
            whisky_attribute = self.get_whisky_orderable_status(whisky)

        return whisky_attribute

    def get_whisky_description(self, whisky):
        return whisky.find('p', class_='shortdesc').get_text()

    def get_whisky_price(self, whisky):
        return whisky.find('span', class_='price').get_text()

    def get_whisky_orderable_status(self, whisky):
        return whisky.find('div', class_='button-box') is not None

    def get_whiskies(self):
        return self.parser.find_all('div', class_='col-xs-12 col-sm-10')

    def get_whisky_information(self, whisky):
        whisky_info = {}
        whisky_info['description'] = self.get_whisky_description(whisky)
        whisky_info['price'] = self.get_whisky_price(whisky)
        whisky_info['orderable'] = self.get_whisky_orderable_status(whisky)
        return whisky_info

    def get_whiskies_information(self):
        whiskies = self.get_whiskies()
        whisky_informations = []
        for whisky in whiskies:
            whisky_informations.append(self.get_whisky_information(whisky))
        return whisky_informations














