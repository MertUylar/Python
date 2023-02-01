
from cmath import sqrt
A=float(input("get the root"))
i=int(input("get a number of iteration"))
x=float(input("get a number of initial guess"))
error=float(input("get the error"))

t=sqrt(x)
print(t)
for c in range(i): 
    x= x-(x*x-A/(2*x))
    print(x)
    if(abs(t-x)<error):
        q=c
        print(q)
        break
    else :
        print("<")
#a yı değiştir

if abs(t-x)< error:
    print("the root could not be found")
    
        