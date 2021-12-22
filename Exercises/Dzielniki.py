# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:46:15 2020

@author: 9
"""
#Program zapyta o liczbę i wyswietli listę dzielników danje liczby

num=int(input("Podaj liczbę: "))
list=[]
for i in range(1,num+1):
    if num%i==0:
        list.append(i)
        
print(list)