# -*- coding: utf-8 -*-
import math

flag=0
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
            
            
            Matris[j][0]=primes[0]
            Matris[j][1]=primes[1]
            
            
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
    total=int(Matris[k][0]*(math.pow(10,digit))+Matris[k][0]+Matris[k][1]+Matris[k][1])
    k+=1 
    for l in range(2,total):
        if total%l==0:
            flag=1
            break
    if flag==0:
        
        print("prime number is {}".format(total))
        
    flag=0    
    print("\ntotal number {}".format(total))
    print("_______________________\n") 
             