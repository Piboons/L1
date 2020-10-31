u = [1, -1]
n = int(input("n "))
if n >= 2:
	for i in range (2, n+1):
		u.append((u[i-1]/2) + 2*u[i-2])
print(u[n])