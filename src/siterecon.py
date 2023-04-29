# python libraries
from time import sleep
# external libraries
from bs4 import BeautifulSoup
import requests
# project imports
from src.display import IO
from tree import Tree

"""
//todo: make a tree for link structure
//todo: make different modes (aggressive, passive, etc)
    //todo: passive mode - randomizes wait time between requests
//todo: option to save logs
todo: save non-domain name links and group them by domain
todo: find and save emails
todo: reports site response status
todo: make settings json file
todo: scan which sites have http
todo: scan which pages have forms on them
todo: separate results by status, http protocol, forms on pages
"""

# soup = BeautifulSoup(page.text, 'html.parser')

class SiteRecon():
    url = None
    root = None
    all_links = set()
    external_links = []
    all_emails = set()
    crawl_count = 0
    crawl_max = None
    pause = 0
    aggression = None
    file_name = None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    def __inti__(self):
        pass

    def title(self):
        IO.display_title()

    def get_http_response(self, url):
        r = requests.get(url, headers=self.headers)
        return r

    def is_external_link(self, link):
        return not self.url in link

    #  Checks if a link is internal or external and adds them to the appropriate list
    def find_page_links(self, soup):
        links = []
        for a_tag in soup.find_all('a'):
            link = a_tag.get('href')
            if self.is_external_link(link):
                self.external_links.append(link)
            else:
                links.append(link)
        return links

    # Adds children nodes to the parent node
    def add_children(self, html, parent):
        soup = BeautifulSoup(html, 'html_parser')
        links = self.find_page_links(soup)
        for link in links:
            child = Tree(link)
            parent.add_child(child)

    def check_for_input_fields(self, html, url):
        soup = BeautifulSoup(html, 'html_parser')
        input_tags = soup.find_all('input')
        if len(input_tags) > 0:
            IO().input_field_found()

    #? Do I need this?
    def check_status_code(self, status):
        first_digit = int(status[0])
        match first_digit:
            case 1:
                return [False]
            case 2:
                return [True]
            case 3:
                return [False]
            case 4:
                return [False]
            case 5:
                return [False]

    # Calls the functions that will scan the page for various items
    def scan_page(self, url, node):
        r = self.get_http_response(url)
        response = self.check_status_code(str(r.status_code))
        if response[0]:
            IO.status_report_good(r.status_code, url)
            self.add_children(r.text, node)
            self.check_for_input_fields(r.text, url)
        else:
            IO.status_report_bad(r.status_code, url)

    # Goes through the tree in a breadth first search
    def crawl_site(self, parent):
        self.crawl_count += 1
        children = parent.get_children()
        # exit case
        if self.crawl_count > self.crawl_max or len(children) == 0:
            return
        # Scan each child url
        for child in children:
            self.scan_page(child.url, child)
        # recursively call children nodes
        for child in children:
            self.crawl_site(child)

    def validate_command(self, command):
        pass

    def target_url(self):
        command = IO.get_command()
        self.validate_command(command)
        r = self.get_http_response("https://" + self.url)
        if r.status_code == 200:
            self.root = Tree("https://" + self.url)
            # call function to get and add root children
            self.crawl_site(self.root)
        else:
            print("add to else statement [target_url]")

    def run_program(self):
        self.title()
        self.target_url()

# Run the program
SiteRecon().run_program()