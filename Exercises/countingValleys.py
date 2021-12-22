# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 05:07:21 2020

@author: 9
"""

def countingValleys(n, s):
    pointner=0
    list=[]
    
    for p in s:
        if p=="U":
            pointner+=1
        elif p=="D":
            pointner-=1
        if pointner == 0 and p == "D":
            list.append("M")
        elif pointner == 0 and p == "U":
            list.append("V")
    
    numValley=list.count("V")
    
    return numValley

s=["U","D","D","D","U","U","D","D","D","U","U","U"]



print(countingValleys(12,s))