from textblob import TextBlob
import string
import random

# This is a very small sample. Take into consideration that you should replace this with a bigger text to
# obtain more cool results.

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

text = ''.join(filter(lambda x: x in string.printable, text) #Remove non-ascii characters the long way
text = text.decode('ascii', errors="ignore") #Remove non-ascii characters the short way
blob = TextBlob(text)
np = blob.noun_phrases
for p in np: print p

for s in blob.sentences: print s # print sentences

# Extract all verbs from the text
nvl = [] # NVL stands for new verb list
for word, tag in blob.tags:
	if tag.startswith("VB"):
		nvl.append(word.lemmatize())


print random.choice(nvl) + " " + random.choice(np) #Print verb + noun randomly