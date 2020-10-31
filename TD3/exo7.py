import random
def deviner():
	nb = random.randint(1,100)
	guess = -1
	while guess != nb:
		guess = int(input("envoie nombre entre 1 et 100\n"))
		if guess < nb:
			print("trop petit")
		elif guess >= nb:
			print("trop grand")
	print("trouvé bg")

def faire_deviner():
	print("pense à un nombre")
	a = 1
	b = 100
	c = int((a+b)/2)
	avis = input(str(c)+"?\n")
	while avis != "trouvé":
		if avis == "plus petit":
			b = c
			c = int((a+b)/2)
		elif avis == "plus grand":
			a = c
			c = int((a+b)/2)
		avis = input(str(c)+"?\n")
	print("bravo")