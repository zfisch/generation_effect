from string import ascii_letters
import random 

def extract_words(string):
	return string.split() 

def remove_letters(word):
	result = word
	if len(word)>5:
		index = random.randint(1, len(word)-2)
		if not result[len(result)-1] in ascii_letters:
			index -= 1 
		result = result[:index] + result[index+1:]
	return result

def mutate_all(submission):
	new_words_list = map(remove_letters, extract_words(submission))
	return ' '.join(new_words_list)
