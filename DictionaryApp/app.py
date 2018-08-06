import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) > 0 :
		yn = raw_input("Did you mean %s instead ? Enter Y if yes, or N if no :"%get_close_matches(word,data.keys())[0])
		if yn == 'Y':
			return data[(get_close_matches(word,data.keys()))[0]]
		else : 
			return "We didn't understand your request"
	else :
		return "We didn't understand your entry"
				
word = raw_input("Enter Word : ")
lst = translate(word)
if type(lst) == list:
	for l in lst:
		print l
else :  
	print lst