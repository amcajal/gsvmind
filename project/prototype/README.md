 THIS IS THE README FOR THE PROTOTYPE OF GSVMind PROJECT
=======================================================
@TODO
Here are listed the contents of the /project/prototype folder, and the description of each element.

**bs4_test.py**: This python script contains a simple test using beautifulsoup version 4. It downloads a webpage, and applies the
library. Several basic operations are performed to test the capabilities of the library.

**random_test.py**: This python script mess around with the random package to generate random numbers.

**get_rn_links.py**: This python script gets random articles from Wikipedia, and in the last one, gets the list of links in the article.

**big_message_printer.py**: This python script prints in the shell or CLI used a "ascii art" message (for example, the words
"GSVmind" but turned into big letters composed of ascii characters). This script bases its functionality in two other files:
	- Ascii_message_to_list.py: Python script that takes the content of a txt file containing an "ascii art" and prints
	in screen the equivalent in python list (that is, turns an ascii art into a python list data type, making it possible
	to copy and paste it into a python code).
	- gsvmind_ascii_message.txt: the ascii art message of the application.
These set of files uses [7] to generate the ascii art.
	
**list_subset.py**: This python script tests how to extract a specific subset from a list of components, and related operations.

**textblob_test.py**: This python script tests the capabilities of textblob library.

**upper_lower_links_test.py**: This python script is used to obtain and aproximation of how many "unique" links are contained in a
	single Wikipedia article, and its related IDs in the total list of them. By unique links it shall be understood those
	links that appear due to the theme in the article, and not those used to proide functionality to the page (i.e: link
	to main page, link to index, link to external references, link to wikipedia features, etc).

**ascii_message_to_list.py**: Python script to test how to turn an ASCII text into a python list, so it can be printed as demanded.

**gsvmind_ascii_message.py**: Text file containing the ASCII text to be turned into a list (used in the previous script).

**div_retrieval_test.py**: Python script to test how to return specific text sections from an HTML, using the div attributes as guide.