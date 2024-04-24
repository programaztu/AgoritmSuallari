n=int(input('Say Girin: '))                                                                                     
a=[0]*n
k=1
from random import randint
for i in range(n):                                                                  
    a[i]=randint(-10,20)
for i in a:
    k*=i
print(k)
