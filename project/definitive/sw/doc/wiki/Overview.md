OVERVIEW
========

The following diagram shows the elements of GSVmind and its relationship:
![gsv_block_diagram](https://github.com/amcajal/gsvmind/blob/master/project/definitive/sw/doc/media/GSVMind_design-GSVMind_Block_Diagram.png)

When the program is launched, GSVmind retrieves a random article from Wikipedia, extracts its text concent, and performs
basic Natural Language Processing operations on it, to obtain an output similar (more or less) to the GSV names appearing
in "The Culture" series by Ian M. Banks.

The generated output (the generated "GSV name") is printed on screen, and saved into a log file, which contains additonal information
for the user amusement:

Screen output:
```
 .d8888b.   .d8888b.  888     888               d8b               888
d88P  Y88b d88P  Y88b 888     888               Y8P               888
888    888 Y88b.      888     888                                 888
888         "Y888b.   Y88b   d88P 88888b.d88b.  888 88888b.   .d88888
888  88888     "Y88b.  Y88b d88P  888 "888 "88b 888 888 "88b d88" 888
888    888       "888   Y88o88P   888  888  888 888 888  888 888  888
Y88b  d88P Y88b  d88P    Y888P    888  888  888 888 888  888 Y88b 888
 "Y8888P88  "Y8888P"      Y8P     888  888  888 888 888  888  "Y88888

GSV operative! It decided to name itself:"Skaffen-Amtiskaw the best"
```

Log information:
```
GSVNAME log
RANDOM_WIKI_URL:https://boraHorzaGobuchul.com
GEN_METHOD:SENTENCES
GSVNAME:Skaffen-Amtiskaw the best
```

The whole application functionality is specified in the requirements.txt document, found under project/def/sw/req. 
The applications entry point is "gsvmind.py", found under project/def/sw/src, which is a perfect place to start div into the
code and how the application is implemented.

A core aspect of the application is the Python language. GSVmind is implemented in Python, 
either custom code or using several libraries, like Requests, BeautifulSoup
and TextBlob. The matching between the Python code and the modules is shown in the following diagram:
![gsv_mapping_tech](https://github.com/amcajal/gsvmind/blob/master/project/definitive/sw/doc/media/GSVMind_design-GSVmind_tech_mapping_diagram.png)

Finally, the project is "fully" tested with a suit of tests found under project/def/sw/test.

