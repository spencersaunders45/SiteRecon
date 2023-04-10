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
"""

# soup = BeautifulSoup(page.text, 'html.parser')

class SiteRecon():
    url = None
    soup = None
    root = None
    current_node = None
    all_links = set()
    all_emails = set()
    crawl_length = 100
    pause = 0
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    def __inti__(self):
        pass

    def title(self):
        IO.display_title()

    def get_http_response(self):
        r = requests.get("https://" + self.url, headers=self.headers)
        return r
    
    def find_links(self, node):
        for href in self.soup:
            pass

    def crawl_site(self):
        loop = True
        while loop:
            sleep(self.pause)
            

    def target_url(self):
        self.url = IO.get_url()
        r = self.get_http_response()
        if r.status_code == 200:
            self.root = Tree(None, "https://" + self.url)
            self.current_node = self.root
            self.crawl_site()
        else:
            print("add to else statement [target_url]")

    def run_program(self):
        self.title()
        self.target_url()
