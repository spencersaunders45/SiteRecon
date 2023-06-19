# python libraries
from time import sleep
import re
from random import randint
from multiprocessing import Process
# external libraries
from bs4 import BeautifulSoup
from requests import get, Response
from rich.progress import Progress
from rich.live import Live
# project imports
from display import IO
from node import Node
from output import Writer

"""
//todo: make a Node for link structure
//todo: make different modes (aggressive, passive, etc)
    //todo: passive mode - randomizes wait time between requests
//todo: option to save logs
todo: save non-domain name links and group them by domain
//todo: find and save emails
todo: reports site response status
//todo: make settings json file
todo: scan which sites have http
todo: scan which pages have forms on them
todo: separate results by status, http protocol, forms on pages
"""


class SiteRecon():
    root = None
    crawl_count = 0
    crawl_max = 25
    pause_min = 5
    pause_max = 13
    aggression = None
    file_name = None
    basic_url = None
    current_url = None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    all_links = set()
    external_links = set()
    all_emails = set()
    urls_with_forms = set()
    phone_numbers = set()
    writer = Writer()
    io = IO(crawl_max)

    def __init__(
            self,
            url: str,
            aggression: str,
            c_aggression: str,
            count: int, 
            file_path: str,
            file_name: str
            ):
        self.target_url = url
        self.aggression = aggression
        self.c_aggression = c_aggression
        self.crawl_max = count
        self.file_name = file_name,
        self.file_path = file_path

    def get_http_response(self, url):
        """Gets the response data from the URL
        
        Parameters:
        url : str
            The website url

        Returns:
            Response
        """
        try:
            r = get(url, headers=self.headers)
            return r
        except Exception as e:
            print(e)
            return Exception

    def is_external_link(self, link: str):
        """Checks if the found url shares the base domain of the root url
        
        Parameters:
        link : str
            The found url on the scanned webpage

        Returns:
            bool
        """
        return self.basic_url in link

    #  Checks if a link is internal or external and adds them to the appropriate list
    def find_page_links(self, soup: BeautifulSoup, url: str) -> None:
        """Finds and sorts links found on scanned webpage
        
        Parameters:
        soup : BeautifulSoup
            The HTML of the scanned webpage
        url : str
            The current webpage url

        Returns:
            list
        """
        links = []
        for a_tag in soup.find_all('a'):
            # Get the link from the a_tag
            link = a_tag.get('href')
            if link == None or len(link) == 0:
                continue
            # Skips single slashes and all #
            if len(link) == 1 and link == "/":
                continue
            if link[0] == "#":
                continue
            # Create full link if needed
            if link[0] == "/":
                link = url + link
            elif "/" not in link and "." not in link:
                link = url + "/" + link
            elif "/" in link and "." not in link and link[0] != "/":
                link = url + "/" + link
            # Extract mailto: links
            if "mailto:" in link:
                split_link = link.split("mailto:")
                self.all_emails.add(split_link[1])
                continue
            # Extract tel: links
            if "tel:" in link:
                tel = link.split("tel:")
                self.phone_numbers.add(tel[1])
                continue
            # Sort links
            if not self.is_external_link(link):
                self.external_links.add(link)
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
        links = self.find_page_links(soup, parent.url)
        for link in links:
            if link not in self.all_links:
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
        input_tags = soup.find_all('input')
        if len(input_tags) > 0:
            self.urls_with_forms.add(url)

    def find_emails(self, soup: BeautifulSoup) -> None:
        """Find the emails in the HTML code
        
        Parameters:
        soup : BeautifulSoup
            The parsed html of the webpage
        url : str
            The webpage url

        Returns:
            None
        """
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        for text in soup.stripped_strings:
            emails = re.search(regex_email, text)
            if emails:
                email_list = emails.group()
                self.all_emails.add(email_list)

    def request_pause(self) -> None:
        """Pauses between requests
        
        Parameters:
            None

        Returns:
            None
        """
        if self.pause_max > 0:
            wait_period = randint(self.pause_min, self.pause_max)
            sleep(wait_period)

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
        # print("SCANNING: ", url)
        self.crawl_count += 1
        self.request_pause()
        r = self.get_http_response(url)
        if r == Exception:
            raise Exception
        self.writer.log_internal_urls(url, r.status_code)
        soup = BeautifulSoup(r.text, 'html.parser')
        self.add_children(soup, node)
        self.check_for_input_fields(soup, url)
        self.find_emails(soup)

    # Goes through the Node in a breadth first search
    def crawl_site(self, parent: Node) -> None:
        """Crawls through all the pages of the website
        
        Parameters:
        parent : Node
            The current node of the web tree

        Returns:
            None
        """
        print(parent.url)
        children = parent.get_children()
        # exit case
        if self.crawl_count > self.crawl_max or len(children) == 0:
            return
        # Scan each child url
        for child in children:
            if self.crawl_count > self.crawl_max:
                break
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

    def create_tree(self) -> None:
        """
        Gets the target url from the user and starts the scan

        Parameters:
            url: the target url for scanning

        Returns:
            None
        """
        # Create the root Node for the website tree
        self.root = Node(self.target_url)
        self.current_url = self.target_url

    def get_basic_url(self) -> None:
        """
        Strips the url from the http text
        """
        basic_url = None
        if "https://www." in self.root.url:
            basic_url = self.root.url.split("https://www.")[1]
        elif "https://" in self.root.url:
            basic_url = self.root.url.split("https://")[1]
        elif "http://www." in self.root.url:
            basic_url = self.root.url.split("http://www.")[1]
        elif "http://" in self.root.url:
            basic_url = self.root.url.split("http://")[1]
        else:
            basic_url = self.root.url
        self.basic_url = basic_url


    def run_program(self) -> None:
        """Starts the process of scanning the website
        
        Parameters:
            None

        Returns:
            None
        """
        self.io.display_title()
        self.create_tree()
        self.get_basic_url()
        self.writer.write_header(self.root.url)
        self.all_links.add(self.root.url)
        progress_proc = Process(target=self.display_progress)
        live_text_proc = Process(target=self.display_current_url)
        progress_proc.start()
        live_text_proc.start()
        try:
            self.scan_page(self.root.url, self.root)
            self.crawl_site(self.root)
        except Exception as e:
            print(e)
            print("A failure occurred")
        # self.scan_page(self.root.url, self.root)
        # self.crawl_site(self.root)
        progress_proc.join()
        live_text_proc.join()
        self.writer.log_data(self.all_emails, self.external_links, self.urls_with_forms, self.all_links)


    def display_progress(self):
        with Progress() as progress:
            scan_progress = progress.add_task("[red]Progress...", total=self.crawl_max)
            last_count = self.crawl_count

            while not progress.finished:
                update = 0
                if self.crawl_count > last_count:
                    update = self.crawl_count - last_count
                    last_count = self.crawl_count
                progress.update(scan_progress, advance=update)
                sleep(1)


    def display_current_url(self):
        with Live() as live:
            while self.crawl_max < self.crawl_count:
                live.update(f"[blue]Scanning: {self.current_url}")
                live.refresh
                sleep(1)