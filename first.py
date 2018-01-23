from __future__ import unicode_literals
import spacy
nlp = spacy.load('/home/aditya/BTechProject/Model/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
document = unicode(open('/home/aditya/BTechProject/Resources/EntityDoc.txt').read().decode('utf8'))
document = nlp(document)
seedList = {"driver", "car", "cars", "rental", "license", "country", "tax", "location", "charge", "request", "group", "model", "day", "customer", "reservations", "time", "date", "booking", "maintenance", "transfer", "mileage", "year", "card", "contract", "penalty", "branch", "requirements", "drivers"}
nouns = {"NN", "NNP", "NNS", "NNPS"}
newList = set("")
flag = 0
temp = ""

for word in document:
	if(flag == 1 and word.text in seedList):
		newList.add(temp + " " + word.text)
		temp = ""
		flag = 0
	elif(flag == 1 and word.text not in seedList and (word.tag_ in nouns or word.tag_ == "JJ")):
		temp = temp + " " + word.text
		flag = 1
	elif(flag == 1 and (word.text not in seedList) and (word.tag_ not in nouns) and (word.tag_ != "JJ")):
		flag = 0
		temp = ""
	elif(flag == 0 and (word.text not in seedList) and (word.tag_ == "JJ")):
		#print(word.text, word.pos_, word.tag_, word.shape_)
		flag = 1
		temp = word.text

flag = 0
tenp = ""

for word in document:
	if(flag == 1 and word.text in seedList):
		newList.add(temp + " " + word.text)
		temp = ""
		flag = 0
	elif(flag == 1 and word.text not in seedList and word.tag_ in nouns):
		flag = 1
		temp = temp + " " + word.text	
	elif(flag == 1 and word.text not in seedList and word.tag_ not in nouns):
		flag = 0
	elif(word.text not in seedList and word.tag_ in nouns):
		#print(word.text, word.pos_, word.tag_, word.shape_)
		flag = 1
		temp = word.text

i = 0
temp = ""

for word in document:
	if(i == 1 and word.text in seedList):
		i = 1
		temp = temp + " " + word.text
	elif(i == 0 and word.text in seedList):
		i = 1
		temp = word.text
	elif(i == 1 and word.text not in seedList and word.tag_ in nouns):
		temp = temp + " " + word.text
	elif(i == 1 and word.text in seedList):
		temp = temp + " " + word.text
	elif(i == 1 and word.text not in seedList and word.tag_ not in nouns):
		newList.add(temp)
		i = 0
		temp = ""

flag = 0
temp = ""
i = 0

for word in document:
	if(i == 3 and word.text in seedList):
		i = 0
		temp = temp + " " + word.text
		newList.add(temp)
	elif(i == 3 and word.text not in seedList):
		i = 0
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
	elif(word.text not in seedList):
		temp = word.text
		i = 1



newList = newList - seedList

for word in newList:
	print(word)
