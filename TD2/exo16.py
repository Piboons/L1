j = int(input("jour "))
m = int(input("mois "))
a = int(input("annee "))
mois = [31,28,31,30,31,30,31,31,30,31,30,31]
if (a%4==0 and a%100 != 0) or a%400 == 0:
	mois[1] = 29

if j >= 31 and m >= 12:
	jdemain = 1
	mdemain = 1
	ademain = a + 1

elif j >= mois[m-1]:
	jdemain = 1
	mdemain = m + 1
	ademain = a

else:
	jdemain = j + 1
	mdemain = m
	ademain = a

print("aujourd'hui: " + str(j) + " " + str(m) + " " + str(a))
print("demain: " + str(jdemain) + " " + str(mdemain) + " " + str(ademain))
