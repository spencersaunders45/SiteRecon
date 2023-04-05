from bs4 import BeautifulSoup
from rich import print
from rich.console import Console
import requests

console = Console()

console.print(" __________   __________   __________   _________     ___________    _________    _________    __________    ____        ___ ", style="bold red")
console.print("|          | |          | |          | |         |   |   _____   |  |         |  |         |  |          |  |     \     |   |", style="bold red")
console.print("|    ______| |___    ___| |___    ___| |    _____|   |  |     |  |  |    _____|  |    _____|  |   ____   |  |      \    |   |", style="bold red")
console.print("|   |            |  |         |  |     |   |         |  |_____|  |  |   |        |   |        |  |    |  |  |       \   |   |", style="bold red")
console.print("|   |______      |  |         |  |     |   |_____    |       ____|  |   |_____   |   |        |  |    |  |  |        \  |   |", style="bold red")
console.print("|          |     |  |         |  |     |         |   |       \      |         |  |   |        |  |    |  |  |    |\   \ |   |", style="bold red")
console.print("|______    |     |  |         |  |     |    _____|   |   |\   \     |    _____|  |   |        |  |    |  |  |    | \   \|   |", style="bold red")
console.print("       |   |     |  |         |  |     |   |         |   | \   \    |   |        |   |        |  |    |  |  |    |  \       |", style="bold red")
console.print(" ______|   |  ___|  |___      |  |     |   |_____    |   |  \   \   |   |_____   |   |_____   |  |____|  |  |    |   \      |", style="bold red")
console.print("|          | |          |     |  |     |         |   |   |   \   \  |         |  |         |  |          |  |    |    \     |", style="bold red")
console.print("|__________| |__________|     |__|     |_________|   |___|    \___\ |_________|  |_________|  |__________|  |____|     \____|", style="bold red")

"""
todo: make a tree for link structure
todo: make different modes (aggressive, passive, etc)
    todo: passive mode - randomizes wait time between requests
todo: option to save logs
todo: save non-domain name links and group them by domain
todo: find and save emails
todo: 
"""
url = "https://www.byui.edu/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# Get site html
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())

# url = input("Enter a URL: ")