def startswith(text, prefix):
	if len(text) == 0:
		return False
	for i in range(0, len(prefix) - 1):
		if text[i] != prefix[i]:
			return False
	return True

def endswith(text, suffix):
	n = len(text)
	m = len(suffix)
	if n == 0:
		return False
	for i in range (0, m):
		if text[n-1-i] != suffix[m-1-i]:
			return False
	return True

vb = input("envoie verbe\n")
if endswith(vb,"er"):
	print("prems groupe trofor")
elif endswith(vb, "ir"):
	print("deuz dsl il fera mieux la prochaine fois")
else:
	print("3e ah la honte")