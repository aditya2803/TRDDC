import spacy

def cleanup(token, lower = True):
	if lower:
		token = token.lower()
	return token.strip()

nlp = spacy.load('/home/aditya/BTechProject/Model/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
document = unicode(open('/home/aditya/BTechProject/Resources/doc1.txt').read().decode('utf8'))
document = nlp(document)
labels = set([w.label_ for w in document.ents])
for label in labels:
	entities = [cleanup(e.string, lower=False)
for e in document.ents if label == e.label_]
	entities = list(set(entities))
	print label, entities

