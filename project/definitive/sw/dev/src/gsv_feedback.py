################################################################################
#   Project: GSVMind
#
#   File: gsv_feedback.py
#
#   Description: Module in charge of print an "ascii art" message 
#				in scheen (when commanded) to provide feedback to
#				the users.
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

# As defined by LLR_035
ASCII_ART_MESSAGE = [

[' ', '.', 'd', '8', '8', '8', '8', 'b', '.', ' ', ' ', ' ', '.', 'd', '8', '8', '8', '8', 'b', '.', ' ', ' ', '8', '8',
 '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
 'd', '8', 'b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8'], # Row 0

['d', '8', '8', 'P', ' ', ' ', 'Y', '8', '8', 'b', ' ', 'd', '8', '8', 'P', ' ', ' ', 'Y', '8', '8', 'b', ' ', '8', '8',
 '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
 'Y', '8', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8'], # Row 1

['8', '8', '8', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', 'Y', '8', '8', 'b', '.', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8',
 '8', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
 ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '8', '8', '8'], # Row 2

['8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', 'Y', '8', '8', '8', 'b', '.', ' ', ' ', ' ', 'Y', '8',
 '8', 'b', ' ', ' ', ' ', 'd', '8', '8', 'P', ' ', '8', '8', '8', '8', '8', 'b', '.', 'd', '8', '8', 'b', '.', ' ', ' ',
 '8', '8', '8', ' ', '8', '8', '8', '8', '8', 'b', '.', ' ', ' ', ' ', '.', 'd', '8', '8', '8', '8', '8'], # Row 3

['8', '8', '8', ' ', ' ', '8', '8', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', '"', 'Y', '8', '8', 'b', '.', ' ', ' ', 'Y',
 '8', '8', 'b', ' ', 'd', '8', '8', 'P', ' ', ' ', '8', '8', '8', ' ', '"', '8', '8', '8', ' ', '"', '8', '8', 'b', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', '"', '8', '8', 'b', ' ', 'd', '8', '8', '"', ' ', '8', '8', '8'], # Row 4

['8', '8', '8', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '"', '8', '8', '8', ' ', ' ', ' ',
 'Y', '8', '8', 'o', '8', '8', 'P', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8'], # Row 5

['Y', '8', '8', 'b', ' ', ' ', 'd', '8', '8', 'P', ' ', 'Y', '8', '8', 'b', ' ', ' ', 'd', '8', '8', 'P', ' ', ' ', ' ',
 ' ', 'Y', '8', '8', '8', 'P', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', 'Y', '8', '8', 'b', ' ', '8', '8', '8'], # Row 6

[' ', '"', 'Y', '8', '8', '8', '8', 'P', '8', '8', ' ', ' ', '"', 'Y', '8', '8', '8', '8', 'P', '"', ' ', ' ', ' ', ' ',
 ' ', ' ', 'Y', '8', 'P', ' ', ' ', ' ', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ',
 '8', '8', '8', ' ', '8', '8', '8', ' ', ' ', '8', '8', '8', ' ', ' ', '"', 'Y', '8', '8', '8', '8', '8'] # Row 7 

]

################################################################################

# As defined by LLR_036, LLR_039
def print_message_line(line_number):
	if ((line_number <= 0) or line_number > len(ASCII_ART_MESSAGE)):
		print "###"
	else:
		row_to_print = ""
		for char in ASCII_ART_MESSAGE[line_number-1]:
			row_to_print += char
		print row_to_print
