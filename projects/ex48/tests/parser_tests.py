from nose.tools import *
from ex48.parser import *
from ex48 import lexicon

def test_parse_sentence():
	tuples = lexicon.scan("eat the princess")
	parsedSentence = parse_sentence(tuples)
	listedSentence = Sentence(('noun', 'player'), ('verb', 'eat'), ('noun', 'princess'))

	assert_equal(parsedSentence.subject, listedSentence.subject)
	assert_equal(parsedSentence.verb, listedSentence.verb)
	assert_equal(parsedSentence.object, listedSentence.object)
	
