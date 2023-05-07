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
    def __init__(self, file_name="output.txt"):
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
        f = open(self.file_name, "w")
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
        f.write("\n========== INTERNAL URL'S ==========\n")
        for url in self.visited_sites:
            f.write(f"{status_code}: {url}\n")
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

    def log_emails(self, emails: set) -> None:
        """Logs the emails found
        
        Parameters:
        emails : list
            All the emails found while scanned

        Returns:
            None
        """
        f = open(self.file_name, "a")
        f.write("\n========== EMAILS ==========\n")
        for email in emails:
            f.write(email+"\n")
        f.close()

    def log_urls_with_forms(self, form_list: set) -> None:
        """
        
        """
        f = open(self.file_name, "a")
        f.write("\n========== WEBPAGES WITH FORMS ==========\n")
        for url in form_list:
            f.write(url + "\n")
        f.close()

    def log_http_sites(self, all_links: set) -> None:
        """
        
        """
        f = open(self.file_name, "a")
        f.write("\n========== HTTP ONLY ==========\n")
        for link in all_links:
            if "https" not in link:
                f.write(link + "\n")
        f.close()

    def log_external_links(self, external_links: set) -> None:
        """Logs the external links found
        
        Parameters:
        external_links : list
            All the external links found on the website

        Returns:
            None
        """
        f = open(self.file_name, "a")
        f.write("\n========== EXTERNAL LINKS ==========\n")
        for link in external_links:
            f.write(link+"\n")
        f.close()

    def log_data(self, emails: set, external_links: set, urls_with_forms: set, all_links: set) -> None:
        """Logs the data found during scanning
        
        Parameters:
        emails : set
            All the emails found during scanning
        external_links : set
            All external links found during scanning
        urls_with_forms : set
            All urls that have forms
        all_links : set
            All links found when scanning
        """
        self.log_emails(emails)
        self.log_external_links(external_links)
        self.log_urls_with_forms(urls_with_forms)
        self.log_http_sites(all_links)
