################################################################################
#   Project: GSVMind
#
#   File: gsv_web_scrapper.py
#
#   Description: gsv_web_scrapper module, in charge of get from internet
#				valid text data and process it, in order to make it available
#				and ready for next modules to be analyzed.
#
#   Notes: N/A
#
#   Contact: Alberto Martin Cajal, amartin.glimpse23<AT>gmail.com
#
#   URL: https://github.com/amcajal/gsvmind
#
#   License: GNU GPL v3.0
#
#   Copyright (C) 2018 Alberto Martin Cajal
#
#   This file is part of GSVMind.
#
#   GSVMind is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   GSVMind is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################
import logging
import requests
import string
from bs4 import BeautifulSoup as beso # So romantic. U got it?

import gsv_error_handler
import gsv_feedback

################################################################################

# This variables works as "enums", without the need of import libraries
NON_VALID_DATA= 1

# These are the error codes related to failures in this module
VALID_PAGE_TEXT_ERROR_CODE = 100

# This string is required to log the random url from wikipedia just
# before leaving the module. Data could be logged in "get_random_wiki_page"
# function, but requirement LLR_006 establishes that log operation
# shall take place before returning the text data.
RANDOM_URL_TO_LOG = ""

################################################################################	
	
# As defined by LLR_008, LLR_009
def get_random_wiki_page():
	# These operations are just to avoid requests module to log undesired data.
	logging.getLogger("requests").setLevel(logging.ERROR)
	logging.getLogger("urllib3").setLevel(logging.WARNING)
	
	random_page = requests.get("https://en.wikipedia.org/wiki/Special:Random")
	if random_page.status_code != 200:
		return NON_VALID_DATA
	else:
		global RANDOM_URL_TO_LOG
		RANDOM_URL_TO_LOG = str(random_page.url)
		return random_page
	

# As defined by LLR_010, LLR_011	
def extract_text_from_page(random_page):
	soup = beso(random_page.content, 'html.parser')
	page_text = ""
	target_divs = soup.findAll('div',attrs={"class":"mw-content-ltr"})
	for td in target_divs:
		page_text += td.find("div").text 

	# This should delete all NON ascii characters that managed to reach this phase
	page_text = ''.join(filter(lambda x: x in string.printable, page_text))
	
	# Perform several checkings to gain more confidence on the text content
	if ((page_text == "") or (len(page_text) == 0)):
		return NON_VALID_DATA
	else:
		return page_text


# As defined by LLR_014, LLR_015
def encode_page_to_ascii(random_page):
	# This operation fails in many situations, so its required to
	# wrap it in a try-except-finally block
	try:
		random_page.content.decode(random_page.encoding).encode('ascii', 'replace')
		return random_page #Now it is encoded in ascii
	except:
		return NON_VALID_DATA
	
	
# As defined by LLR_007, LLR_012, LLR_013
def get_valid_text_content():
	# Operation is considered failed by default. If it succeed, then
	# it will be changed to True, and trigger proper operations.
	is_operation_successfull = False 
	attempts = 5
	while (attempts > 0):
		random_page = get_random_wiki_page()
		if random_page == NON_VALID_DATA:
			attempts -= 1
			continue
			
		page_encoded_in_ascii = encode_page_to_ascii(random_page)
		if page_encoded_in_ascii == NON_VALID_DATA:
			attempts -= 1
			continue
			
		page_text = extract_text_from_page(page_encoded_in_ascii)
		if page_text == NON_VALID_DATA:
			attempts -= 1
			continue
			
		is_operation_successfull = True
		break
	
	if is_operation_successfull != True:
		gsv_error_handler.handle_error(VALID_PAGE_TEXT_ERROR_CODE)
	else:
		return page_text


# As defined by LLR_016	
# At this moment, this function is quite useless, as it could be put
# inline. However, in the future, more advanced processing could be
# required, so it is left as it is.
def apply_further_processing(only_ascii_text):
	return 	only_ascii_text.replace(";", ".").replace("\"", ".").replace("\'", ".")	
	
	
# As defined by LLR_006
def get_text_data():
	# All calls to gsv_feedback, as defined by LLR_037 
	gsv_feedback.print_message_line(1)
	
	valid_text_content = get_valid_text_content()
	gsv_feedback.print_message_line(2)
	
	processed_text = apply_further_processing(valid_text_content)
	gsv_feedback.print_message_line(3)
	
	#As defined by LLR_027 and LLR_029
	logging.info("RANDOM_URL:"+ RANDOM_URL_TO_LOG)
	gsv_feedback.print_message_line(4)
	
	return processed_text	
