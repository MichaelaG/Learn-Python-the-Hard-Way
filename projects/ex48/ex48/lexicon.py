# Exercise 48

def scan(string) :

	directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat']
        stops = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'bear', 'princess', 'cabinet']
	
	# take in a string of characters
	# break those characters apart by separating at spaces - use "split"

	words = string.split()
	returned_tuples = []

	# determine what kind of object each "piece" is - ie number or word

	def is_number(word):
		try:
			return int(word)
		except ValueError:
			return None

 	#compare the words with those stored in the tuple - nouns/verbs/directions/stops/numbers stored for comparison

	for word in words:

		if word in directions:
			returned_tuples.append(('direction', word))
			
		elif word in verbs:
			returned_tuples.append(('verb', word))

		elif word in stops:
			returned_tuples.append(('stop', word))
	
		elif word in nouns:
			returned_tuples.append(('noun', word))

	# if word is not in the lexicon, then return the word with an "error" connected to it

		else:
			check = is_number(word)
			if check == None:
				returned_tuples.append(('error', word))
			else:
				returned_tuples.append(('number', check))

	# return all the tuples for the sentence the user inputted	

	return returned_tuples
