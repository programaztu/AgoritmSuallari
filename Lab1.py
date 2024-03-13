n = 1
x = 0.5
P = 0
e = (x ** n) / n
while e >= 0.01:
    P += e
    n+=1
    e= -e
print(P)
