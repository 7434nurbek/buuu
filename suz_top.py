import random
from uzwords import words

def get_word():
	word = random.choice(words)
	while "_" in word or " "in word:
		word = random.choice(words)
	return word.upper()

def display(user_latters,word):
	display_latter = ""
	for latter in word:
		if latter in user_latters.upper():
			display_latter = display_latter+latter
		else:
			display_latter = display_latter+'-'
	return display_latter

def play():
	word = get_word()
	word_latters = set(word)
	user_latters = ''
	print(f"Мен {len(word)} хонали сон уйладим , топа оласизми?")
	while len(word_latters)>0:
		print(display(user_latters,word))
		if len(user_latters)>0:
			print(f"шу вактгача киритган харфларингиз {user_latters}")
		latter = input('харф киритинг>>>').upper()
		if  latter in user_latters:
			print("бу харфни аввал киритгансиз! бошка харфни киритинг>>>")
			continue
		elif latter in word:
			word_latters.remove(latter)
			print(f"{latter} harfi to`g`ri")
		else :
			print("бундай сон йук")
		user_latters += latter
		print(f"табриклайман {word} cyзини {len(user_latters)} та уринишда топдингиз ")
play()