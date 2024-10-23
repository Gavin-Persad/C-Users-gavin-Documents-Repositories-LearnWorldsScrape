import requests
from bs4 import BeautifulSoup

def scrape_and_save(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(soup.prettify())

scrape_and_save(
    "https://learn.schoolofcode.co.uk/path-player?courseid=soc-onboarding&unit=65be2ca7536e31c52c0c3388Unit", 
    'output.md'
)