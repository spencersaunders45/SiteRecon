# python libraries
from time import sleep
# external libraries
from bs4 import BeautifulSoup
import requests
# project imports
from display import IO
from tree import Tree

"""
todo: make a tree for link structure
todo: make different modes (aggressive, passive, etc)
    todo: passive mode - randomizes wait time between requests
todo: option to save logs
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
    soup = None
    root = None
    all_links = set()
    all_emails = set()
    crawl_count = 0
    crawl_max = 100
    pause = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    def __inti__(self):
        pass

    def title(self):
        IO.display_title()

    def get_http_response(self, url):
        r = requests.get(url, headers=self.headers)
        return r
    
    def find_links(self, parent):
        links = []
        for href in self.soup:
            link = href.get('href')
            if link not in self.all_links:
                child_node = Tree(parent, link)

    def scan_page(self, url):
        r = self.get_http_response(url)
        # check status code
        # get page links & separate from external links
        # check for forms
        # 

    """
    1. get links of root and add to children
    2. start looping through children and add their child links
    3. once looped through all them 
    """
    def crawl_site(self, parent):
        self.crawl_count += 1
        children = parent.get_children()
        # exit case
        if self.crawl_count > self.crawl_max or len(children) == 0:
            return
        # Scan each child url
        for child in children:
            # call function to scan url page
            pass
        # recursively call children nodes
        for child in children:
            self.crawl_site(child)

    def target_url(self):
        self.url = IO.get_url()
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