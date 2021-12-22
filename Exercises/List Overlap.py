# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:16:37 2020

@author: 9
"""
import numpy as np

list1 = np.random.randint(89,size=(1, 20))
list2 = np.random.randint(89,size=(1, 20))


#I sposób
newList=[]

for a in list1[0]:
    if a in list2[0]:
        if a in newList:
            continue
        newList.append(a)

print(newList)

#II sposób
#Zapisz wszytko w jednej linjce--jeszcze nie udane!!!
newList=[a for a in list1[0] if a in list2[0]]
print(newList)