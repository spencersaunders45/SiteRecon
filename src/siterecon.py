# python libraries
from time import sleep
# external libraries
from bs4 import BeautifulSoup
import requests
# project imports
from src.display import IO
from node import Node

"""
//todo: make a Node for link structure
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
    """Runs the application
    
    Attributes:
    url : str
        The root URL
    root : Node
        The root of the Node
    all_links : set
        A set of all collected links with the same given base domain
    crawl_count : int
        The number of sites scanned
    crawl_max : int
        The max number of sites to scan
    pause_min : int
        The minimum time to wait before requesting another site
    pause_max : int
        The max time to wait before requesting another site
    aggression : str
        The aggression mode 
    file_name : str
        The name of the output file
    headers : str
        The headers sent in the request
    """
    url = None
    root = None
    crawl_count = 0
    crawl_max = None
    pause_min = None
    pause_max = None
    aggression = None
    file_name = None

    def __inti__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
        self.all_links = set()
        self.external_links = []
        self.all_emails = set()

    def get_http_response(self, url):
        """Gets the response data from the URL
        
        Parameters:
        url : str
            The website url

        Returns:
            Response
        """
        r = requests.get(url, headers=self.headers)
        return r

    def is_external_link(self, link: str):
        """Checks if the found url shares the base domain of the root url
        
        Parameters:
        link : str
            The found url on the scanned webpage

        Returns:
            bool
        """
        return not self.url in link

    #  Checks if a link is internal or external and adds them to the appropriate list
    def find_page_links(self, soup: BeautifulSoup):
        """Finds and sorts links found on scanned webpage
        
        Parameters:
        soup : BeautifulSoup
            The HTML of the scanned webpage

        Returns:
            list
        """
        links = []
        for a_tag in soup.find_all('a'):
            link = a_tag.get('href')
            if self.is_external_link(link):
                self.external_links.append(link)
            else:
                links.append(link)
        return links

    # Adds children nodes to the parent node
    def add_children(self, html, parent: Node) -> None:
        """Adds links found on the scanned webpage to the parent Node
        
        Parameters:
        html : Response
            The response text from the url request
        parent : Node
            The parent node

        Returns:
            None
        """
        soup = BeautifulSoup(html, 'html_parser')
        links = self.find_page_links(soup)
        for link in links:
            child = Node(link)
            parent.add_child(child)

    def check_for_input_fields(self, html, url: str) -> None:
        """Checks if the scanned webpage has any input fields
        
        Parameters:
        html : Response
            The text value of the webpage response
        url : str
            The webpage url

        Returns:
            None
        """
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

    def scan_page(self, url: str, node: Node) -> None:
        """Scans the html of the page
        
        Parameters:
        url : str
            The webpage url
        node : Node
            The current node being scanned

        Returns:
            None
        """
        r = self.get_http_response(url)
        response = self.check_status_code(str(r.status_code))
        if response[0]:
            IO.status_report_good(r.status_code, url)
            self.add_children(r.text, node)
            self.check_for_input_fields(r.text, url)
        else:
            IO.status_report_bad(r.status_code, url)

    # Goes through the Node in a breadth first search
    def crawl_site(self, parent: Node) -> None:
        """Crawls through all the pages of the website
        
        Parameters:
        parent : Node
            The current node of the web tree

        Returns:
            None
        """
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

    def target_url(self) -> None:
        """Gets the target url from the user and starts the scan

        Parameters:
            None

        Returns:
            None
        """
        command = IO.get_command()
        self.validate_command(command)
        r = self.get_http_response("https://" + self.url)
        if r.status_code == 200:
            self.root = Node("https://" + self.url)
            # call function to get and add root children
            self.crawl_site(self.root)
        else:
            print("add to else statement [target_url]")

    def run_program(self) -> None:
        """Starts the process of scanning the website
        
        Parameters:
            None

        Returns:
            None
        """
        IO.display_title()
        self.target_url()

# Run the program
SiteRecon().run_program()