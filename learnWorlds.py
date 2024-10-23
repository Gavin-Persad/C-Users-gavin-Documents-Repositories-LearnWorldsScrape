import requests
from bs4 import BeautifulSoup

def scrape_and_save(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write(soup.prettify())

scrape_and_save(
    "https://learn.schoolofcode.co.uk/author/pageseditor?page=ebook667931af9ce0f110a50f7467-667931b027143&type=ebook&from=course&course-title-id=bc17-on&unit-id=667931af9ce0f110a50f7467&direct=1", 
    'output.md'
)