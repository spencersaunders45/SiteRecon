# python libraries
from time import sleep
import re
# external libraries
from bs4 import BeautifulSoup
from requests import get, Response
# project imports
from display import IO
from node import Node

"""
//todo: make a Node for link structure
//todo: make different modes (aggressive, passive, etc)
    //todo: passive mode - randomizes wait time between requests
//todo: option to save logs
todo: save non-domain name links and group them by domain
todo: find and save emails
todo: reports site response status
//todo: make settings json file
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
    crawl_max = 10
    pause_min = None
    pause_max = None
    aggression = None
    file_name = None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    all_links = set()
    external_links = []
    all_emails = set()

    def __inti__(self):
        pass

    def get_http_response(self, url):
        """Gets the response data from the URL
        
        Parameters:
        url : str
            The website url

        Returns:
            Response
        """
        r = get(url, headers=self.headers)
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
    def add_children(self, soup: BeautifulSoup, parent: Node) -> None:
        """Adds links found on the scanned webpage to the parent Node
        
        Parameters:
        soup : BeautifulSoup
            The parsed html of the webpage
        parent : Node
            The parent node

        Returns:
            None
        """
        links = self.find_page_links(soup)
        for link in links:
            child = Node(link)
            parent.add_child(child)

    def check_for_input_fields(self, soup: BeautifulSoup, url: str) -> None:
        """Checks if the scanned webpage has any input fields
        
        Parameters:
        soup : BeautifulSoup
            The parsed html of the webpage
        url : str
            The webpage url

        Returns:
            None
        """
        # todo: write findings to report
        input_tags = soup.find_all('input')
        if len(input_tags) > 0:
            IO().input_field_found()

    def find_emails(self, soup: BeautifulSoup, url: str) -> None:
        """Find the emails in the HTML code
        
        Parameters:
        soup : BeautifulSoupu
            The parsed html of the webpage
        url : str
            The webpage url

        Returns:
            None
        """
        # todo: write findings to report
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        for text in soup.stripped_strings:
            emails = re.search(regex_email, text)
            if emails:
                email_list = emails.group()
                self.all_emails.add(email_list)


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
        self.crawl_count += 1
        r = self.get_http_response(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.add_children(soup, node)
        self.check_for_input_fields(soup, url)
        self.find_emails(soup, url)

    def crawl_root_page(self):
        """Crawls the root page and adds the children
        
        Parameters:
            None

        Returns:
            None
        """
        self.crawl_count += 1
        url = self.root.url
        r = self.get_http_response(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.add_children(soup, self.root)
        self.check_for_input_fields(soup, url)
        self.find_emails(soup, url)

    # Goes through the Node in a breadth first search
    def crawl_site(self, parent: Node) -> None:
        """Crawls through all the pages of the website
        
        Parameters:
        parent : Node
            The current node of the web tree

        Returns:
            None
        """
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

    def validate_command(self, command: str):
        pass

    def split_commands(self, command: str) -> str:
        """Turns the command into a list
        
        Parameters:
        command : str
            The commands entered by the user

        Returns:
            list
        """
        parsed_command = command.split(' ')
        return parsed_command

    def return_url(self, command_list: list) -> str:
        """Returns the url from the command list
        
        Parameters:
        command : list
            The list of commands given by the user

        Returns:
            str : The target url
        """
        url = command_list[0]
        if 'http' in url or 'https' in url:
            return url
        else:
            return "https://" + url

    def target_url(self) -> None:
        """Gets the target url from the user and starts the scan

        Parameters:
            None

        Returns:
            None
        """
        command = IO().get_command()
        # self.validate_command(command)
        command_list = self.split_commands(command)
        target_url = self.return_url(command_list)
        # Create the root Node for the website tree
        self.root = Node(target_url)

    def run_program(self) -> None:
        """Starts the process of scanning the website
        
        Parameters:
            None

        Returns:
            None
        """
        IO().display_title()
        self.target_url()
        self.crawl_root_page()
        self.crawl_site(self.root)

        for email in self.all_emails:
            print(email)
        for link in self.all_links:
            print(link)
        print("External URLs: ", self.external_links)


# Run the program
SiteRecon().run_program()