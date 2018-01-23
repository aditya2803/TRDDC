import spacy
from nltk import Tree
nlp = spacy.load('/usr/local/lib/python2.7/site-packages/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0')
document = unicode(open('/home/aditya/BTechProject/Resources/GovtDoc.txt').read().decode('utf8'))
document = nlp(document)
def to_nltk_tree(node):
	if node.n_lefts + node.n_rights > 0 :
		return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
	else :
		return node.orth_
[to_nltk_tree(sent.root).pretty_print() for sent in document.sents]
