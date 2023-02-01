
from cmath import sqrt

i=int(input("get a number of iteration"))
x=int(input("get a number of initial guess"))
error=int(input("get the error"))
t=sqrt(x)
for c in range(i): 
    
    xnew= x-(x*x-400/2*x)
    
    if(abs(t-xnew)<error):
        q=c
        break


if abs(t-xnew)< error:
    print("the root could not be found")
    
        