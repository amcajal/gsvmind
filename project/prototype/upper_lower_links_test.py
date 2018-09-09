from bs4 import BeautifulSoup as besup # Rename to besup to call it easily
import requests # To get html pages

'''
None entries in lists, and strings with non-ascii characters give a lot of problems
when trying to write them into a file, so the easies way is to try to perform the
operation, and if an exception arises, ignore it.
'''
def write_to_file(file_name, list):
	writer = open(file_name, 'w')
	for link in list:
		try:
			content = str(link) + "\n"
			writer.write(content)
		except:
			pass
	writer.close()

###################
page = requests.get("https://en.wikipedia.org/wiki/Space_Invaders")
soup = besup(page.content, 'html.parser')
link_list = [x.get('href') for x in soup.find_all('a')]
write_to_file("space_invaders.links", link_list);

page = requests.get("https://en.wikipedia.org/wiki/International_Space_Station")
soup = besup(page.content, 'html.parser')
link_list = [x.get('href') for x in soup.find_all('a')]
write_to_file("iss.links", link_list);

