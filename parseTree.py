import spacy
from spacy import displacy
nlp = spacy.load('/usr/local/lib/python2.7/site-packages/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
document = unicode(open('/home/aditya/BTechProject/Resources/GovtDoc.txt').read().decode('utf8'))
document = nlp(document)
for ent in document:
	print(ent.text, ent.dep_, ent.head.text, ent.head.pos_, [child for child in ent.children])


