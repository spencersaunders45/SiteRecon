import datetime

"""
todo: Add header to output. Default header is the main URL and time it was scanned
todo: add ability to customize output file name
"""

class Writer:
    """Writes the output file of the information gathered from the website
    
    Attributes:
    file_name : str
        The name of the output file
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.visited_sites = list()

    def write_header(self, url: str) -> None:
        """Writes the header on the report file
        
        Parameters:
        url : str
            The main page url

        Returns:
            None
        """
        time_data = datetime.datetime.now()
        date = time_data.strftime("%x")
        time = time_data.strftime("%X")
        f = open(self.file_name, "a")
        f.write(f"================= {url} [{time} {date}] =================\n")
        f.close()

    def log_internal_urls(self, url: str, status_code: int) -> None:
        """Logs that status codes of internal pages
        
        Parameters:
        url : str
            The webpage url
        status_code : int
            The returned status code

        Returns:
            None
        """
        f = open(self.file_name, "a")
        f.write("========== INTERNAL URL'S ==========")
        for url in self.visited_sites:
            f.write(f"{status_code}: {url}")
        f.close()

    def write_log(self, text: str) -> None:
        """Writes the colleted data to the output file
        
        Parameters:
        text : str
            The text to be written to the output file

        Returns:
            None
        """
        f = open(self.file_name, "a")
        f.write(text + "\n")
        f.close()

    def add_url(self, status_code: int, url: str) -> None:
        """Adds the url to the list
        
        Parameters:
        status_code : int
            The status code returned from the http request
        url : str
            The url link

        Returns:
            None
        """
        site = [status_code, url]
        self.visited_sites.append(site)

    def log_emails(self, emails: list) -> None:
        """Logs the emails found
        
        Parameters:
        emails : list
            All the emails found while scanned

        Returns:
            None
        """
        f = open(self.file_name, "a")
        f.write("========== EMAILS ==========")
        for email in emails:
            f.write(email)
        f.close()

    def log_external_links(self, external_links: list) -> None:
        """Logs the external links found
        
        Parameters:
        external_links : list
            All the external links found on the website

        Returns:
            None
        """
        f = open(self.file_name, "a")
        f.write("========== EXTERNAL LINKS ==========")
        for link in external_links:
            f.write(link)
        f.close()

    def log_data(self, emails: list, external_links: list) -> None:
        self.log_emails(emails)
        self.log_external_links(external_links)
