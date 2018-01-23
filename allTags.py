from __future__ import unicode_literals
import spacy
nlp = spacy.load('/home/aditya/BTechProject/Model/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
document = unicode(open('/home/aditya/BTechProject/Resources/GovtDoc.txt').read().decode('utf8'))
document = nlp(document)
for word in document:
	print(word.text, word.pos_, word.tag_, word.shape_)
