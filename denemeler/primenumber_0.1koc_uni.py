# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:34:25 2022

@author: ozkan
"""
j=0
number = int(input("Enter a random number: "))
primes = []
w=20
h=20
Matris=[[0 for z in range(w)]for y in range(h)]

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
            print("prime numbers: ",primes)
            
            Matris[j][0]=primes[0]
            Matris[j][1]=primes[1]
            
            print(Matris[j][0])
            print(Matris[j][1])
            j+=1
        
        