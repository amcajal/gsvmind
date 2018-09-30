![project_logo](https://github.com/amcajal/gsvmind/blob/master/project/definitive/sw/doc/media/gsvmind_logo.png)

[![Build Status](https://travis-ci.org/amcajal/gsvmind.svg?branch=master)](https://travis-ci.org/amcajal/gsvmind)
[![Coverage](https://img.shields.io/badge/Coverage-91%25-brightgreen.svg)
[![GitHub license](https://img.shields.io/github/license/amcajal/gsvmind.svg)](https://github.com/amcajal/gsvmind/blob/master/LICENSE)


<!--- PROJECT SUMMARY/OVERVIEW -->
Did you hear about [Space X's drone ships called _Of Course I Still Love You_ and _Just Read the Instructions_?](https://www.space.com/28445-spacex-elon-musk-drone-ships-names.html)
Their names are a tribute to
[_The Culture_ books series by Ian M. Banks](https://en.wikipedia.org/wiki/The_Culture), 
a sci-fiction saga where one of the main attractions are the **General System Vehicles**
(or **GSV**): enormous self-conscious spaceships that choose their own names - cool, funny and creepy at equal parts.

GSVmind (* wink wink *) generates random names similar to those of the books. You can use them to name your drone, arduino robot,
microwave, laundry machine or whatever you want.

GSVmind is a python application that uses as its core the [Requests library](http://docs.python-requests.org/en/master/), 
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) 
and [TextBlob](https://textblob.readthedocs.io/en/dev/) 
to extract from Internet the text data 
required to generate the random names - specifically from [Wikipedia, through its awesome service of _Get a random article_](https://en.wikipedia.org/wiki/Special:Random). 
(Kindly consider [donate](https://donate.wikimedia.org/wiki/Ways_to_Give?rdfrom=%2F%2Ffoundation.wikimedia.org%2Fw%2Findex.php%3Ftitle%3DWays_to_Give%2Fen%26redirect%3Dno)
 to one of the best websites in the world).

Besides its funny purpose, GSVmind is an state-of-the-art/sandbox project, where several Principles, Patters and Practices (also known
as P.P.P) has been tried or exercised as a learning process. Some of them are: 
- Test Driven Development
- Requirements Development
- Code Coverage
- Clean Code (readability, modularity, meaningfull comments...)

More information at the [Wiki of the project](https://github.com/amcajal/gsvmind/wiki).

---

## Index
1. [Quickstart](#quickstart)
2. [Contributions](#contributions)
3. [License](#license)
4. [Contact](#contact)

---

### Quickstart

* Clone repo to local computer and go to main directory:

    `$ git clone https://github.com/amcajal/gsvmind.git`
    
    `$ cd <clone_dir>/gsvmind`
    
* Run _setup.sh_ script. If dependencies are not satisfied, you can
run _gsvmind_install_dep.sh_:

    `$ sh setup.sh`
    
    `$ cd /project/def/sw/scripts`
    
    `$ sudo sh gsvmind_install_dep.sh`
    
* If _setup.sh_ finished sucessfully, you can launch now GSVmind from the root directory!:

    `$ python gsvmind.py`
    
Output is generated (it takes between 30 sec to 1 min to be complete) as follows:
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

And of course, take a look to the generated log:
```
GSVNAME log
RANDOM_WIKI_URL:https://boraHorzaGobuchul.com
GEN_METHOD:SENTENCES
GSVNAME:Skaffen-Amtiskaw the best
```
    
* To launch tests individually:

    `$ cd /project/def/sw/tests/`
    
    `$ python <name_of_test_file>.py`

[Back to index](#index)


### License

Alberto Martin Cajal is the original author of **GSVmind** project.
**GSVmind** project is released under GNU GPL version 3.0 license. 
[Check LICENSE file](https://github.com/amcajal/gsvmind/blob/master/LICENSE) 
for a full version of it, or 
[visit the official GNU web page](https://www.gnu.org/licenses/gpl-3.0.html).

[Back to index](#index)



### Contributions

GSVmind is open to contributions! [Check the related page at the Wiki of the project](https://github.com/amcajal/gsvmind/wiki/Contributions).

[Back to index](#index)


### Contact
Alberto Martin Cajal at:
 
- Gmail: amartin.glimpse23@gmail.com (amartin DOT glimpse23 AT gmail DOT com)
- [Blogspot](http://glimpse-23.blogspot.com.es/)
- [LinkedIn](https://es.linkedin.com/in/alberto-martin-cajal-b0a63379)
- Twitter: @amartin_g23

[Back to index](#index)

---

#### This project has been created trying to make it usefull. This project has been created in order to learn new things. But over all, this project has been created because it is fun. As Isaac Asimov said:

*The most exciting phrase to hear in science, the one that heralds new discoveries, is not 'Eureka' but 'That's funny...'*

