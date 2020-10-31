nb = int(input("nombr "))
premier = None
for i in range (2, round(nb/2) + 1):
	if nb%i == 0:
		print("ce nbre es po premierr :((")
		premier = False
		break
if premier != False:
	print("c premier :)")