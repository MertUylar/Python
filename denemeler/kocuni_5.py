# -*- coding: utf-8 -*-


number1=3
number2=5

n=0

while(n<10):
    
       for i in range(2,number1):
         for k in range(2,number2):
              if number1%i !=0:
                  if number2%k !=0:
        
                    print("({},{})".format(number1,number2))
                    
       if number1>number2:
          number2+=1
       if number2>number1:
          number1+=1
       n+=1
                
                    
         
    
       
    
    
    
    
    
   
