# -*- coding: utf-8 -*-
import numpy as np
j=0
i=2
x=int(input("enter first number:"))
y=int(input("enter second number:"))
w=20
h=20
a=1
k=0
Matris=[[0 for z in range(w)]for y in range(h)]

while(x<1 or y<1):
    print("{} number and {} number are not bigger than 1 ".format(x,y))
    x=int(input("enter first number:"))
    y=int(input("enter second number:"))    
    if x>1 and y>1:
        break
        
        
while x<y:
    Matris[k][j]=x
    
    print("numberr  of {}".format(Matris[k][j]))
    for i in range(2,x+1):
        if x%i==0:
            
            Matris[j][a]=i
            
            print(Matris[j][a])
        a+=1
    print("\n")     
    a=1
    j+=1    
    x+=1
         

