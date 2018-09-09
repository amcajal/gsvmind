NOTES
=====

This page contains the notes generated during the application development. The notes are kept for further usage and documentation
purposes, but they shall not be used as reference for the current application status (functionality, structure, etc). Such information
is located under project/def folder.

****
@TODO
To use BeautifulSoup, first we need to download the library. [1] Contains all required information. We executed
	$ sudo apt-get install bs-4
Now we are ready to use it. To download the HTML of the pages, nothing more shall be installed. [2] is a very good tutorial
to do this.
As html example, we are going to use the [3].
To obtain random articles at wikipedia, we just need to make a GET request to the URL of [6]

The Natural Language Processing (NLP) part is more complicated. First, a little of research is necessary [8]. As a first try,
we are going to use the NLTK, following the official webpage at [9].

But textblob [10] seems to be more appropiate. In fact, textblob uses NLTK, so
everything is fine (we can use both libraries if we want). 
First, install it following the instructions of the official webpage:
$ pip install -U textblob
$ python -m textblob.download_corpora

Running a simple script to test the capabilities of textblob (textblob_test.py) shows that a processing of only 8 lines of very small length
took near 15 seconds, so this is a big problem, considering that the real text to be processed (obtained from FULL html pages)
can reach 700 lines of a very large length.

Probably we will need to extract random sections from the text of the article, and apply the library only on those.
Anyways: 
	- The noun_phrases is a good start to obtain random names, but it can be better.
	- The blob.sentences is good to obtain the sentences in the text, but it must be tailored for our purposes.
	
Probably. we will end needing to classify the phrases manually [11].

There is an EXTRAORDINARY tutorial on Textblob on [12], and some of the examples suits really well with our purposes!

The way the app chooses the name of the ship:
	- A noun_phrase
	- A sentence, when colons and quotes has been replaced with dots in the original text.
	- A random selection of verb and noun_phrase.
