OVERVIEW
========

The following diagram shows the elements of GSVmind and its relationship:
(diagram @TODO)

When the program is launched, GSVmind retrieves a random article from Wikipedia, extracts its text concent, and performs
basic Natural Language Processing operations on it, to obtain an output similar (more or less) to the GSV names appearing
in "The Culture" series by Ian M. Banks.

The generated output (the generated "GSV name") is printed on screen, and saved into a log file, which contains additonal information
for the user amusement:

(screen @TODO)
(log example @TODO)

The whole application functionality is specified in the requirements.txt document, found under project/def/sw/req. 
The applications entry point is "gsvmind.py", found under project/def/sw/src, which is a perfect place to start div into the
code and how the application is implemented.

A core aspect of the application is the Python language. GSVmind is implemented in Python, 
either custom code or using several libraries, like Requests, BeautifulSoup
and TextBlob. The matching between the Python code and the modules is shown in the following diagram:
(diagram with tools @TODO)

Finally, the project is "fully" tested with a suit of tests found under project/def/sw/test.

