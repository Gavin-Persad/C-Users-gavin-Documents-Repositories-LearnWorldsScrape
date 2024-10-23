import requests
from bs4 import BeautifulSoup
import urllib.parse

def login_and_scrape(url, username, password, output_file):
    session = requests.Session()
    
    # Replace with the actual login URL of the website
    login_url = "https://learn.schoolofcode.co.uk/"

     # Step 1: Access the login page to get any CSRF tokens
   
    login_page = session.get(login_url)

    # Debugging: Print the login page content to inspect the CSRF token field
    print("Login Page Content:")
    print(login_page.text)

    
    # Step 2: Parse the login page for hidden CSRF token (if present
    soup = BeautifulSoup(login_page.text, "html.parser")
    
     # Look for CSRF token in a hidden input field
    csrf_token = soup.find("input", {"name": "Q9xs6iCiMxn9uBdTUG98IiYAD9LLmfx33EIm3erBN4U-1729687356-1.2.1.1-731E_E1BeODnmNvTTkqycfPplAhzXrY5sZNPRGHdL4KjPRPQXP9hzxitYt0UiR4xdjjsR6T5qMpYKY43xoN3cIAqn0nI4BKpm9ZSUWKndepM80jy18nx1GEta1AkpfmTFM_T4Jb1ZH6ds0YaYxcM2a3pEWccf3izXQ3UdR52Fp.kpx6kqCIILlhT9k4HAPBWIzqzOJhhWRPhWaR16EbCnPebZnqM0MdyUWrdKwdqIlIlvR74cnRX5Iq1NHsdQj9pasvfCfEwG76XIqmsm9Uy98WLy9UZlyQBPGw8.hPUxnfZMpTC7qnG60YuPO95dgtI3tzezbaj9L73d_uacpgN.p.2ynpMm7Q28p44PLfqsnEVEPKtNlafd2TNwXlvnFbl1HdsAqP9M11gyIsrGgaMCQ; twk_idm_key=SQMkdHHHnJOlXQO0eJFt4"})
    token_value = csrf_token["value"] if csrf_token else None

    # Debugging: Print the CSRF token value
    print(f"CSRF Token: {token_value}")
    
    # Data for login form, adjust 'username' and 'password' keys if the form expects different field names
    # Step 3: Prepare login form data including the CSRF token
    login_data = {
        'username': username,
        'password': password,
        'csrf_token': token_value
    }

    # Step 4: Perform the login POST request
    login_response = session.post(login_url, data=login_data)
    
    # Step 5: Check if login was successful
    if login_response.status_code != 200 or "login" in login_response.url:
        
        print("Login failed or redirected to login page. Please check credentials.")
        return
    
    print("Logged in successfully!")

    # Step 7: After login, access the target page (learner's view)
    response = session.get(url)
    
    if response.status_code == 200:
        # Step 8: Parse and save the content of the learner view page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(soup.prettify())
        
        print(f"Page scraped and saved to {output_file}")
    else:
        print(f"Failed to access the learner page. Status code: {response.status_code}")

# Example usage:
login_and_scrape(
    "https://learn.schoolofcode.co.uk/path-player?courseid=bc17-on&unit=667931af9ce0f110a50f7467Unit",  # Learner page URL
    "gavinapersad@gmail.com",  # Replace with your actual username
    "FellowsSoup4@",  # Replace with your actual password
    'output.md'  # Output file to save the scraped HTML
)
