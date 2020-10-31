import math
import random
total = 0
ecarttype = 0
for i in range (0, 1000):
	a = random.random()
	total += a
	ecarttype += a*a
moyenne = total/1000
ecarttype = math.sqrt((ecarttype/1000)-moyenne*moyenne)
print(moyenne)
print(ecarttype)