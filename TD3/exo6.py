def find_substring(text, query, start=0):
	n = len(text)
	m = len(query)
	for i in range (start,n):
		found = True
		for j in range (0, m):
			if text[i+j] != query[j]:
				found = False
				break
		if found:
			return i
	return -1

def count_substring(text, query):
	count = 0
	i = 0
	n = len(text)
	m = len(query)
	while i <= n-m+1:
		if find_substring(text,query,i) >= 0:
			count +=1
			i+=m
		else:
			return count
	return count