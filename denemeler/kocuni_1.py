# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 16:33:56 2022

@author: ozkan
"""

number = int(input("Enter a random number: "))

for num in range(1, number + 1):
    prime = True
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
    if prime:
        print(num)