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


    def selet_tag_by_index(self, children ,index):
        return children[index]

    def get_tag_text(self, tag):
        return tag.get_text()

