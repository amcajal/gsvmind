from bs4 import BeautifulSoup as besup
import requests

ran_url = "https://en.wikipedia.org/wiki/Special:Random"

for i in range(0, 3):
	page = requests.get(ran_url)
	soup = besup(page.content, 'html.parser')
	print soup.title

links = soup.find_all('a')
print len(links)