import requests
from bs4 import BeautifulSoup

def web_scraper(insert_url):
    page = requests.get(insert_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('h1')
    status = page.status_code
    res = result.text

# checking site availabilty result
if status != 200:
    print('Emergency! problem in site at the moment...')
    
elif 'Welcome' not in res:
    print('Emergency! problem in site at the moment...')
else:
    print('Site currently running...')
       

web_scraper('http://localhost')
