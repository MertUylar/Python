

o=0
t=1

print("enter two positive number")
a=int(input())
b=int(input())

while(a<1 or b<1):
    print("try again, enter two positive number")
    a=int(input())
    b=int(input())
    
    
for i in range(a+1):
    c=o
    o=o+t    
    t=c
    print(t)
for i in range(b+1):
    o=0
    t=1
    c=o
    o=o+t   
    t=c
    print(t)    