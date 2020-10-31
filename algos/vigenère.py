alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def chiffrer(m,c):
    n = len(m)
    chiffr = []
    for i in range (0, n):
        chiffr.append(alphabet[(alphabet.index(c[i%len(c)]) + alphabet.index(m[i]))%26])
    return chiffr
def dechiffrer(m, c):
    m = m.lower()
    n = len(m)
    dechiffr = []
    for i in range (0,n):
        dechiffr.append(alphabet[(alphabet.index(m[i]) - alphabet.index(c[i%len(c)])) % 26])
    return dechiffr