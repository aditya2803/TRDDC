from __future__ import unicode_literals
import spacy
nlp = spacy.load('/home/aditya/BTechProject/Model/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
document = unicode(open('/home/aditya/BTechProject/Resources/GovtDoc.txt').read().decode('utf8'))
document = nlp(document)
nouns = {"NN", "NNP", "NNS", "NNPS"}
newList = set("")
flag = 0
temp = ""

for word in document:
	if((flag == 1 or flag == 2) and ((word.tag_ in nouns) or (word.tag_ == "JJ"))):
		temp = temp + " " + word.text
		flag = 2
	elif(flag == 2 and (word.tag_ not in nouns) and (word.tag_ != "JJ")):
		newList.add(temp)
		temp = ""
		flag = 0
	elif(flag == 1 and (word.tag_ not in nouns) and (word.tag_ != "JJ")):
		flag = 0
	elif(flag == 0 and (word.tag_ == "JJ")):
		#print(word.text, word.pos_, word.tag_, word.shape_)
		flag = 1
		temp = word.text

flag = 0
temp = ""

for word in document:
	if(word.tag_ in nouns):
		if(temp == ""):
			temp = word.text
		else:
			temp = temp + " " + word.text	
	elif(word.tag_ not in nouns):
		newList.add(temp)
		temp = ""

i = 1
temp = ""
flag = 0

for word in document:
	if(i == 3 and word.tag_ in nouns):
		i = 0
		temp = temp + " " + word.text
		newList.add(temp)
		temp = ""
	elif(i == 3 and word.tag_ not in nouns):
		i = 1
		temp = ""
	elif(i == 2):
		i = 3
		temp = temp + word.text
	elif(i == 1 and word.text == "-"):
		i = 2
		temp = temp + "-"
	elif(i == 1 and word.text != "-"):
		i = 1
		temp = word.text

flag = 0

for word in document:
	if(flag == 0  and word.tag_ == "CD"):
		temp = word.text
		flag = 1
	elif(flag == 1 and word.tag_ in nouns):
		temp = temp + " " + word.text
		flag = 0
		newList.add(temp)
		temp = ""
	else:
		flag = 0
		temp = ""

flag = 0

for word in document:
	if(word.tag_ in nouns):
		if(temp == ""):
			temp = word.text
		else:
			temp = temp + " " + word.text
		flag = 1
	elif(flag == 1 and word.tag_ == "CD"):
		temp = temp + " " + word.text	
		newList.add(temp)
		flag = 0
	else:
		temp = ""
		flag = 0
flag = 0
for word in document:
	if(((word.tag_ == "NNP") or (word.tag_ == "NNPS")) and flag != 2):
		if(temp == ""):
			temp = word.text
		else:
			temp = temp + " " + word.text
		flag = 1
	elif((flag == 1) and ((word.text == "of") or (word.text == "on"))):
		temp = temp + " " + word.text
		flag = 2
	elif((flag == 2) and ((word.tag_ == "NNP") or (word.tag_ == "NNPS"))):
		flag = 3
		temp = temp + " " + word.text
	elif((word.tag_ != "NNP") and (word.tag_ != "NNPS")):
		if(flag == 3):
			newList.add(temp)
		temp = ""
		flag = 0	
for word in newList :
	print word
