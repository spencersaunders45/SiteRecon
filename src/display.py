from rich.console import Console
from rich.progress import Progress
console = Console()

class IO:
    """A console interface
    
    Attributes:
    title : str
        title: The application title
    """
    title = """
     __________   __________   __________   _________     ___________    _________    _________    __________    ____        ___ 
    |          | |          | |          | |         |   |   _____   |  |         |  |         |  |          |  |     \     |   |
    |    ______| |___    ___| |___    ___| |    _____|   |  |     |  |  |    _____|  |    _____|  |   ____   |  |      \    |   |
    |   |            |  |         |  |     |   |         |  |_____|  |  |   |        |   |        |  |    |  |  |       \   |   |
    |   |______      |  |         |  |     |   |_____    |       ____|  |   |_____   |   |        |  |    |  |  |        \  |   |
    |          |     |  |         |  |     |         |   |       \      |         |  |   |        |  |    |  |  |    |\   \ |   |
    |______    |     |  |         |  |     |    _____|   |   |\   \     |    _____|  |   |        |  |    |  |  |    | \   \|   |
           |   |     |  |         |  |     |   |         |   | \   \    |   |        |   |        |  |    |  |  |    |  \       |
     ______|   |  ___|  |___      |  |     |   |_____    |   |  \   \   |   |_____   |   |_____   |  |____|  |  |    |   \      |
    |          | |          |     |  |     |         |   |   |   \   \  |         |  |         |  |          |  |    |    \     |
    |__________| |__________|     |__|     |_________|   |___|    \___\ |_________|  |_________|  |__________|  |____|     \____|
    """


    def __init__(self, crawl_max):
        self.crawl_max = crawl_max
        self.progress = Progress()
        self.progress_bar = self.progress.add_task("Scanning", total=crawl_max, start=False, visible=True)


    def display_title(self) -> None:
        """Display the application title"""
        console.print(self.title, style="bold red")


    def get_command(self) -> str:
        """Gets the input from the user"""
        command = input("> ")
        return command


    def status_report_bad(self, status_code: int, url: str) -> None:
        """Reports a bad site status code 
        
        Parameters:
        status_code : int
            The status code reported from the site
        url : str
            The website url

        Returns:
            None
        """
        console.log(f"[[bold red]{status_code}[/bold red]]: [blue underline]{url}[/blue underline]")


    def status_report_good(self, status_code: int, url: str) -> None:
        """Reports a good status code
        
        Parameters:
        status_code : int
            The status code reported from the site
        url : str
            The website url

        Returns:
            None
        """
        console.log(f"[[bold green]{status_code}[/bold green]]: [blue underline]{url}[/blue underline]")


    def input_field_found(self, url: str) -> None:
        """Reports url pages where input fields are found
        
        Parameters:
        url : str
            The website url

        Returns:
            None
        """
        console.log(f"[[bold green]✓[/bold green]]: [blue underline]{url}[/blue underline]")


    def update_progress(self, url: str, count: int) -> None:
        """Displays the progress of the search

        Parameters:
        url:
            The current site that is being searched

        Returns:
            None
        """
        if count <= 1:
            self.progress.start_task(self.progress_bar)
        self.progress.update(self.progress_bar, advance=1)


    def display_defaults(self) -> None:
        """Reports that a settings.json file was not found"""
        try:
            f = open("settings.json", "r")
            settings = f.read()
            f.close()
            console.print(settings)
        except:
            console.print("[[red]x[/red]] No settings file found.")
