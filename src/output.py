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
        """
        f = open(self.file_name, "a")
        f.write(text + "\n")
        f.close()

    def add_url(self, status_code: int, url: str) -> None:
        site = [status_code, url]
        self.visited_sites.append(site)