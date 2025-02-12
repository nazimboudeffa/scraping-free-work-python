import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://www.free-work.com/fr/tech-it/jobs'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Find all job titles on the page
    job_titles = soup.find_all('h3', class_='text-lg leading-8 font-bold mb-1 flex justify-between font-semibold text-xl mb-4')
    
    # Print the job titles
    for title in job_titles:
        print(title.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")