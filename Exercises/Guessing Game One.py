# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 03:31:07 2020

@author: 9
"""
import random
num = random.randint(1,9)
gues=input("Odgadnij moją liczbę z zakresu od 1 do 9: ")
trials=1
while gues.upper() !="KONIEC":
    
    if int(gues)<num:
        print("Za mała liczba spróbuj jeszcze raz.")
    elif int(gues)>num:
        print("Za duża liczba spróbuj jeszcze raz.")
    else:
        print("Odgadłe(a)s moją liczbę jest to {}, a twoja to {}. Potrzebowałe(a)s {} prób".format(num, gues, trials))
        break
    gues=input("Odgadnij moją liczbę z zakresu od 1 do 9, lub zakończ program wpisując 'KONIEC'.: ")
    trials+=1