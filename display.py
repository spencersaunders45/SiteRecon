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

    def get_command(self):
        command = input("> ")
        return command

    def status_report_bad(self, status_code, url):
        console.log(f"[[bold red]{status_code}[/bold red]]: [blue underline]{url}[/blue underline]")

    def status_report_good(self, status_code, url):
        console.log(f"[[bold green]{status_code}[/bold green]]: [blue underline]{url}[/blue underline]")

    def input_field_found(self, url):
        console.log(f"[[bold green]input found[/bold green]]: [blue underline]{url}[/blue underline]")

    def display_help(self):
        """ 
        todo: 
        """
        message = """
        Aggressiveness:
            -A: There is no pause between requests. Requests are made as fast as possible.
            -M: There is a 5 to 10 second pause between requests.
            -P: There is a 15 to 30 second pause between requests.
            -C [max wait] [min wait]: This is a custom wait time where you choose the maximum and minimum wait times.

        Output Files:
            -fn [filename]: Allows you to customize the file name.

        Change defaults:
            -Dag [A/M/P/C] [optional-max wait] [optional-min wait]: Change the default aggression type
            -Dfn [filename]: Changes the default file name
        """