
gsv_mind_title = [

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

for row in gsv_mind_title:
    row_to_print = ""
    for char in row:
        row_to_print = row_to_print + char
    print row_to_print