# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:06:35 2020

@author: 9
"""

list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#list2 = []
#for a in list:
#    if a < 5:
#        list2.append(a)
#
#print(list2)


#list2=[a for a in list if a<5]
#print(list2)
num = int(input("Podaj liczbę: "))
list3=[a for a in list if a<num]
print(list3)