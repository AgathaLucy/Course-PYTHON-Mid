# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:35:49 2020

@author: 9
"""

def rotLeft(a, d):
    for i in range(d):
        letter=list.pop(0)
        list.append(letter)
    return list

list=[1,2,3,4,5]


print(rotLeft(list,4))