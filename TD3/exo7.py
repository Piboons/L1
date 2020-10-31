import random

nb = random.randint(1,100)
guess = -1
while guess != nb:
	guess = int(input("envoie nombre entre 1 et 100\n"))
	if guess < nb:
		print("trop petit")
	elif guess >= nb:
		print("trop grand")
print("trouvé bg")