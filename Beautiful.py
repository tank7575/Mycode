import requests
from bs4 import BeautifulSoup
import parser

result = requests.get('https://www.google.com/')

#print(result.status_code)

#https://en.wikipedia.org/wiki/list_of_http_status_codes

print(result.headers)

src = result.content
#print(src)

soup = BeautifulSoup(src, 'html.parser')

links = soup.find_all("a")
#print(links)
#print('\n')

for link in links:
    if 'About' in link.text:
        print(link)
        print(link.attrs['href'])
