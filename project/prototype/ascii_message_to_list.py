def ascii_to_list():
    file_with_ascii_text = ""
    assert file_with_ascii_text != "" # Modify this in the code
    reader = open("", 'r')
    content = reader.read()
    reader.close()
    
    content = content.split("\n")
    content = filter(None, content)
    
    n_lines = len(content)
    for id, line in enumerate(content):
        new_line = ""
        n_chars = len(line)
        for char in range(0, n_chars):
            if char == n_chars-1:
                last_part = "'"
            else:
                last_part ="', "
                
            new_line = new_line + "'" + line[char] + last_part
        if id == n_lines-1:
            last_part = "] # Row "
        else:
            last_part = "], # Row "
        print "[" + new_line + last_part + str(id) + " \n"
            
ascii_to_list()    