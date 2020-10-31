import os
jours = ["dimanche","lundi","mardi","mercredi","jeudi","vendredi","samedi"]
jour = int(input("jour:"))
mois = int(input("mois:"))
annee = int(input("annee:"))
if mois >= 3:
	m = mois-2
	a = annee
else:
	m = mois+10
	a = annee - 1
s = int(str(annee)[0] + str(annee)[1])
anneesiecle = int(str(annee)[2] + str(annee)[3])
f = jour + anneesiecle + anneesiecle//4 - 2*s + s//4 + (26*m - 2)//10
reste = f%7
joursemaine = jours[reste]
print(joursemaine)
os.system("pause")