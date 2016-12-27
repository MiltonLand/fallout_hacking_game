import random

def gibberish_code():
	"""Returns a list of the gibberish code."""
	variable = 0
	index = 48
	gibberish = []

	while True:
		if index >= 71:
			index = 48
		if not (58 <= index <= 64):
			variable += 1
			if variable <= 16:
				if variable % 3 == 0:
					gibberish.append("0xF9" + chr(index))
				gibberish.append("0xF9" + chr(index))
			elif 16 < variable <= 32:
				if variable % 3 == 0:
					gibberish.append("0xFA" + chr(index))
				gibberish.append("0xFA" + chr(index))
			else:
				if variable % 3 == 0:
					gibberish.append("0xFB" + chr(index))
				gibberish.append("0xFB" + chr(index))
		index += 1

		if variable > 47:
			break
	lista = ["8", "4", "0", "C"]

	lista2 = []

	for i in range(0, len(gibberish), 4):
		for j in lista:
			lista2.append(j)

	for i in range(len(gibberish)):
		gibberish[i] += lista2[i]

	return gibberish

def gibberish_str():
	"""Returns a string of gibberish symbols."""
	symbols = []
	for i in range(33, 48):
		if not i == 38:
			symbols.append(chr(i))
		
	for i in range(58, 65):
		symbols.append(chr(i))

	for i in range(91, 96):
		symbols.append(chr(i))

	symbols.append("{")
	symbols.append("|")
	symbols.append("}")
	gibberish_s = ""
	index = 0
	while index < 408:
		gibberish_s += symbols[random.randrange(29)]
		index += 1
	
	return gibberish_s

def replace_word(s1, s2, index):
	"""
	Given 2 strings and an index, replaces the characters in s1 index,
	for the characters in s2
	Args:
		s1: String. 'Long' string.
		s2: String. Word.
		index: number.
	Returns:
		String.
	Example:
		replace_word('Hello world', 'earth', 6)
		'Hello earth'
	"""
	new_str = s1
	i = index
	for j in range(len(s2)):
		new_str = new_str[:i] + s2[j] + new_str[i+1:]
		i += 1 

	return new_str

def add_words_to_gib_st(l):
	"""
	Adds words from a list of words to a gibberish 
	string, and returns that string.
	"""
	gib_str = gibberish_str()
	for i in l:
		random_index = random.randrange(408-len(i)-2)
		gib_str_rand_i = gib_str[random_index]
		if random_index > 1:
			prev_char = gib_str[random_index-2]
		else:
			prev_char = gib_str[random_index]
		last_char = gib_str[random_index+(len(i)-1)]
		next_2_char = gib_str[random_index+(len(i)+1)]
		
		check_index = gib_str_rand_i.isalpha()
		check_last = last_char.isalpha()
		check_prev = prev_char.isalpha()
		check_next2 = next_2_char.isalpha()
		char_check = check_index or check_last or check_prev or check_next2
		
		while char_check:
			random_index = random.randrange(408-len(i)-2)
			gib_str_rand_i = gib_str[random_index]
			if random_index > 1:
				prev_char = gib_str[random_index-2]
			else:
				prev_char = gib_str[random_index]
			last_char = gib_str[random_index+(len(i)-1)]
			next_2_char = gib_str[random_index+(len(i)+1)]
			
			check_index = gib_str_rand_i.isalpha()
			check_last = last_char.isalpha()
			check_prev = prev_char.isalpha()
			check_next2 = next_2_char.isalpha()
			char_check = check_index or check_last or check_prev or check_next2
		
		gib_str = replace_word(gib_str, i, random_index)
		
	return gib_str
