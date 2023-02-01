
pack = input("Enter one from three different packages:  ")
Smc = float(input("what time you call Same operator calls:  "))
Lc = float(input("what time you call Landline calls calls:  "))
Ooc= float(input("what time you call other operator calls:  "))

print("your choice is:"+ pack)

if Smc or Lc or Ooc <0 :
    print("false")
 

elif pack== 'A' or pack== 'a':
    S=0.35 
    L=0.40
    O=0.60
    total=round((Smc*S)+1.5+(Lc*L)+(Ooc*O))
   
    print(total)
elif pack=='B' and pack=='b':
    S=0.35
    L=0.35
    O=0.35
    total=round((Smc*S)+5.00+(Lc*L)+(Ooc*O))
    print(total)
else :
    S=0.10
    L=0.20
    O=0.30
    total=round((Smc*S)+10.00+(Lc*L)+(Ooc*O))
    print(total)

   
 