import math
P=0
siyahi =list(map(int,input('Ededleri Bosluq Buraxaraq Daxil et: ').split()))
for i in siyahi:
    if i>9:
        P+=i
print(P)
