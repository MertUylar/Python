i=0
for sayi in range(1,100):
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               
               break
       else:
           dizi=[0 for z in range(20)]
           dizi[z]=sayi
           print(dizi[z])
           