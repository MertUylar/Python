# -*- coding: utf-8 -*-
import math


n=10
j=0
k=0
number =32
primes = []
add=[]
w=2
h=20
a=2
q=20
Matris=[[0 for z in range(w)]for y in range(h)]
Finals=[[0 for c in range(a)]for n in range(q)]
for num in range(1, number + 1):
    prime = True
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
    if prime:
        primes.append(num)
        
        lent=len(primes)
        
        if lent==3:
            primes.pop(0)
            print("_________")
            
            Matris[j][0]=primes[0]
            Matris[j][1]=primes[1]
            
            print(Matris[j][0])
            print(Matris[j][1])
            j+=1
print("**************")       
while k<j:
    print(Matris[k][0])
    print(Matris[k][1])
    
    a=(Matris[k][1])
    digit=1
    while a>9:
        a=a%10
        digit+=1
    total=(Matris[k][0]*(math.pow(10,digit)))
    total+=Matris[k][0]+Matris[k][1]+Matris[k][1]
    print(total)
    print("**************") 
    k+=1         