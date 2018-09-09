from bs4 import BeautifulSoup as besup # Rename to besup to call it easily
import requests # To get html pages

page = requests.get("https://en.wikipedia.org/wiki/Space_Invaders")
if page.status_code != 200:
	print "Error retrieving the web page. Aborting script"
	exit(1)

soup = besup(page.content, 'html.parser')
writer = open("./space_invaders.txt", 'w')
writer.write(soup.get_text().encode('utf-8')) # Add the encode to avoid "UnicodeEncodeError"
writer.close()