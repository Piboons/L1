def dechiffrer(m, c):
    n = len(m)
    msg = []
    if n%c == 0:
        col = n//c
    else:
        col = n//c + 1
    print(col)
    k = 0
    for i in range (0, c):
        for j in range (0, col):
            msg.append(m[i+j*c])
            k += 1
    return msg