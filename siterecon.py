from bs4 import BeautifulSoup
import requests
from display import IO

"""
todo: make a tree for link structure
todo: make different modes (aggressive, passive, etc)
    todo: passive mode - randomizes wait time between requests
todo: option to save logs
todo: save non-domain name links and group them by domain
todo: find and save emails
todo: reports site response status
"""
IO.display_title()

url = input("Enter a URL: ")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# Get site html
page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())