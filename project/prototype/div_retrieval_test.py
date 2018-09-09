from bs4 import BeautifulSoup as besup # Rename to besup to call it easily
import requests # To get html pages
import string

page = requests.get("https://en.wikipedia.org/wiki/Space_Invaders")
if page.status_code != 200:
	print "Error retrieving the web page. Aborting script"
	exit(1)


soup = besup(page.content, 'html.parser')

text = ""
table = soup.findAll('div',attrs={"class":"mw-content-ltr"})
for x in table:
	text += x.find("div").text 

text = ''.join(filter(lambda x: x in string.printable, text))

writer = open("./space_invaders_only_divs.txt", 'w')
writer.write(text) 
writer.close()
