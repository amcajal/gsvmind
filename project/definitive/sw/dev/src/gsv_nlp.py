################################################################################
#   Project: GSVMind
#
#   File: gsv_nlp.py
#
#   Description: Module in charge of process the input text data 
#				to generate random English phrases (the GSVMind name)
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
import sys
import random
import re
from textblob import TextBlob

import gsv_error_handler
import gsv_feedback

################################################################################

# Error code related with a failure in this module
INVALID_OUTPUT = 200

# These variables works as enums, without using external libraries.
NOUN_PHRASE = 0
SENTENCES = 1
VERB_PLUS_NOUN = 2

GENERATION_METHODS = [NOUN_PHRASE, SENTENCES, VERB_PLUS_NOUN]

################################################################################

def get_lemmatize_verbs(blob):
	nvl = [] # NVL stands for new verb list
	for word, tag in blob.tags:
		if tag.startswith("VB"):
			nvl.append(word.lemmatize())
	return nvl


# As defined by LLR_019, LLR_030
def get_noun_phrase(np):
	if np:
		return random.choice(np)
	else:
		return ""
	
	
# As defined by LLR_021, LLR_030
def get_sentence(sen):
	if sen:
		return random.choice(sen)
	else:
		return ""
	

# As defined by LLR_022, LLR_030	
def get_verb_plus_noun(verbs, np):
	if np and verbs:
		return random.choice(verbs) + " " + random.choice(np)
	else:
		return ""
	
	
# As defined by LLR_020
def is_output_valid(output):
	words = output.split(" ")
	words = filter(None, words)
	if ( (len(words) > 0) and (len(words) <= 5) ):
		return True
	else:
		return False
	
	
# As defined by LLR_046	
def postprocess(input_text):
	output = re.sub(r'[^a-zA-Z]', ' ', input_text)
	output = re.sub(r'\s *', ' ', output).strip().title()
	return output
	
	
# As defined by LLR_017, LLR_018, LLR_023, LLR_024	
def generate_english_phrase(input_ascii_text):
	# All calls to gsv_feedback as defined in LLR_038
	gsv_feedback.print_message_line(5)
	
	# If the output generation fails, repeat all the TextBlob operations
	# would take too much time. So its data is calculated just once.
	blob = TextBlob(input_ascii_text) 
	np = blob.noun_phrases
	sen = blob.sentences
	verbs = get_lemmatize_verbs(blob)

	attempts = 5
	while (attempts > 0):
		# Choose randomly the output generation method
		selected_method = random.choice(GENERATION_METHODS)
		
		# Generate output using the chosen generation method
		output = ""
		
		#This is just for the logging functionality
		gen_method = ""
		if selected_method == NOUN_PHRASE:
			output = get_noun_phrase(np)
			gen_method = "NOUN_PHRASE"
			
		elif selected_method == SENTENCES:
			output = get_sentence(sen)
			gen_method = "SENTENCES"
			
		elif selected_method == VERB_PLUS_NOUN:
			output = get_verb_plus_noun(verbs, np)
			gen_method = "VERB_PLUS_NOUN"
			
		else:
			# Unknwon error, just abort execution. It could be considered
			# as a failure when generating a valid output, but a failure
			# when trying to select an entry from a well defined list
			# is considered severe (failure in the OS, or in the Python
			# interpreter).
			gsv_error_handler.handle_error(9999)

		# Cast to string 
		output = str(output)
		output = postprocess(output)
		
		# Check output compliance with UR_001
		if is_output_valid(output):
			gsv_feedback.print_message_line(6)
			break
		else:
			attempts -= 1
		
	if attempts == 0:
		gsv_error_handler.handle_error(INVALID_OUTPUT)
		
	gsv_feedback.print_message_line(7)
	
	# As defined by LLR_033
	logging.info("GEN_METHOD:"+gen_method+"\nGSVNAME:"+output)
	
	gsv_feedback.print_message_line(8)
	
	# Return output
	return output
