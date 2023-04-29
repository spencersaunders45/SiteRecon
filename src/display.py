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
        console.log(f"[[bold green]✓[/bold green]]: [blue underline]{url}[/blue underline]")

    def invalid_c_flag(self):
        console.log(f"[[bold red]x[/bold red]]: max wait or min wait is not a number.")

    def invalid_filename(self, file_name):
        console.log(f"[[bold red]x[/bold red]]: {file_name} cannot be a filename")

    def invalid_symbol(self):
        console.print('[[bold red]x[/bold red]]: the following symbols cannot be used in a filename [. \ / " * | ? : > <]')

    def invalid_aggression_parameter(self, flag):
        console.print(f'[[bold red]x[/bold red]]: {flag} is not a valid parameter for -Dag')

    def invalid_path(self, path):
        console.print(f"[[bold red]x[/bold red]]: {path} is not a valid path")

    def not_a_number(self, value):
        console.print(f'[[bold red]x[/bold red]]: {value} is not a number')

    def display_help(self):
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

    def display_defaults(self):
        try:
            f = open("settings.json", "r")
            settings = f.read()
            f.close()
            console.print(settings)
        except:
            console.print("[[red]x[/red]] No settings file found.")
