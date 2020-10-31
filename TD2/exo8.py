import os
somme = int(input("somme: "))
monnaie = {500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
res = str(somme) + " "
for key in monnaie.keys():
	while somme >= key:
		monnaie[key] += 1
		somme -= key
	if monnaie[key] != 0:
		res += str(key) + " x " + str(monnaie[key]) + " "
print(res)
os.system("pause")