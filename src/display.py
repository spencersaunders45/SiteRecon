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

    def invalid_c_flag(self) -> None:
        """Reports the improper use of the -c flag"""
        console.log(f"[[bold red]x[/bold red]]: max wait or min wait is not a number.")

    def invalid_filename(self, file_name: str) -> None:
        """Reports an invalid filename
        
        Parameters:
        file_name : str
            The name of the output file

        Returns:
            None
        """
        console.log(f"[[bold red]x[/bold red]]: {file_name} cannot be a filename")

    def invalid_symbol(self) -> None:
        """Reports a symbol that cannot be used"""
        console.print('[[bold red]x[/bold red]]: the following symbols cannot be used in a filename [. \ / " * | ? : > <]')

    def invalid_aggression_parameter(self, flag: str) -> None:
        """Reports an invalid use of the -Dag flag
        
        Parameters:
        flag : str
            The parameter send with the -Dag flag

        Returns:
            None
        """
        console.print(f'[[bold red]x[/bold red]]: {flag} is not a valid parameter for -Dag')

    def invalid_path(self, path: str) -> None:
        """Reports and invalid output path
        
        Parameters:
        path : str
            The given folder path

        Returns:
            None
        """
        console.print(f"[[bold red]x[/bold red]]: {path} is not a valid path")

    def not_a_number(self, value: str) -> None:
        """Reports that a value is not a number
        
        Parameters:
        value : str
            The value that is not a number

        Returns:
            None
        """
        console.print(f'[[bold red]x[/bold red]]: {value} is not a number')

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

    def display_help(self) -> None:
        """Displays the flags"""
        message = """
        Aggressiveness:
            -A: There is no pause between requests. Requests are made as fast as possible.
            -M: There is a 5 to 15 second pause between requests.
            -P: There is a 15 to 30 second pause between requests.
            -C [max wait] [min wait]: This is a custom wait time where you choose the maximum and minimum wait times.

        Output Files:
            -fn [filename]: Allows you to customize the file name.
            -fp [output path]: Changes the output path of the file.
                • The given file path must be the absolute file path.

        Change defaults:
            -Dag [A/M/P/C] ['C only' max wait] ['C only' min wait]: Change the default aggression type.
            -Dfn [filename]: Changes the default file name.
            -Dfp [output path]: Changes the default output path.
            -Ds [number]: Changes the default number of sites searched.

        Sites searched:
            -s [number]: Changes the number of sites searched. Default is 20.

        Default settings:
            -D: Displays the default settings.
        """
        console.print(message, style="grey")

    def display_defaults(self) -> None:
        """Reports that a settings.json file was not found"""
        try:
            f = open("settings.json", "r")
            settings = f.read()
            f.close()
            console.print(settings)
        except:
            console.print("[[red]x[/red]] No settings file found.")
