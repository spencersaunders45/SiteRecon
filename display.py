from rich.console import Console
console = Console()

class IO:
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

    def __init__(self):
        pass

    def display_title(self):
        console.print(self.title, style="bold red")

    def get_url(self):
        url = input("Enter a URL: ")
        return url

    def status_report_bad(self, status_code, url):
        console.log(f"[[bold red]{status_code}[/bold red]]: [blue underline]{url}[/blue underline]")

    def status_report_good(self, status_code, url):
        console.log(f"[[bold green]{status_code}[/bold green]]: [blue underline]{url}[/blue underline]")

    def input_field_found(self, url):
        console.log(f"[[bold green]input found[/bold green]]: [blue underline]{url}[/blue underline]")