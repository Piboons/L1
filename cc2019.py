def exo1():
	z = int(input("nombre z:\n"))
	if z > 0:
		if z%2==0:
			print("z est pair")
		else:
			print("z est impair")
	elif z == 0:
		print("z est nul")
	else:
		print("la valeur absolue de z vaut " + str(-z))

def exo2():
	i = 2
	u = 0
	while True:
		u = 3**i + i**4 - 3
		print("pour i = " + str(i) + ", u = ", str(u))
		if u >= 1000000:
			print(i)
			break
		else:
			i += 2

#exo3
def f(u):
	if u%2 == 0:
		return u/2 + 2
	else:
		return 7*u

def powf(u,n):
	res = u
	for i in range (0,n):
		res = f(res)
	print(res)