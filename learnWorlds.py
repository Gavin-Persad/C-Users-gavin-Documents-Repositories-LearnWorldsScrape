import requests
from bs4 import BeautifulSoup

def login_and_scrape(url, username, password, output_file):
    session = requests.Session()
    
    # Replace with the actual login URL of the website
     # Step 1: Access the login page to get any CSRF tokens
    login_url = "https://learn.schoolofcode.co.uk/"
    login_page = session.get(login_url)

    
    # Step 2: Parse the login page for hidden CSRF token (if present
    soup = BeautifulSoup(login_page.text, "html.parser")
    
     # Look for CSRF token in a hidden input field
    csrf_token = soup.find("input", {"name": "4d951f865555be3f8672e6c6ef5ca388f427764d8473a67aab21932b683da2eb"}) # Replace 'csrf_token' with actual token name
    token_value = csrf_token["value"] if csrf_token else None
    
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
    "r.kozachenko2000@gmail.com",  # Replace with your actual username
    "Work'2024",  # Replace with your actual password
    'output.md'  # Output file to save the scraped HTML
)