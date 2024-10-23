import requests
from bs4 import BeautifulSoup

def login_and_scrape(url, username, password, output_file):
    session = requests.Session()
    login_url = 'https://example.com/login'  # Replace with the actual login URL
    data = {
        'username': username,
        'password': password
    }

    session.post(login_url, data=data)

    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(soup.prettify())

    

login_and_scrape(
    "https://learn.schoolofcode.co.uk/path-player?courseid=bc17-on&unit=667931af9ce0f110a50f7467Unit",
    "gavinapersad@gmail.com", 
    "FellowsSoup4@",
    'output.md'
)