# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:58:30 2020

@author: 9
"""

dict = {"czesc": "hello", "mama": "mother", "tata": "father", "pies": "dog"}
while True:
   polish_word = input("Podaj słowo po polsku: ")
   if polish_word in dict: 
        print("Słowo po angielsku to: ", dict[polish_word]) 
   elif polish_word=="0":
       print("zakończenie pracy słownika")
       break
   else:
       print("Nie znaleziono słowa w słowniku.")