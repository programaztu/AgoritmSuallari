import math
y=0
a=2
x=0.5
e=math.cos(a*x)/((a-1)*(a+1))
while e>0.001:
    e=math.cos(a*x)/((a-1)*(a+1))
    y+=e
    a+=2
print(y)
