# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 06:02:32 2020

@author: 9
"""

#def jumpingOnClouds(c):

c = [0,1,0,0,0,1,0]

jump=0
counter = 0

while jump < len(c)-1:

    if (jump+2<=len(c)-1) and c[jump+2] == 0:
        jump+=2
        counter+=1
    elif c[jump+1] == 0:
        jump+=1
        counter+=1
   

print(counter)

#definicja rekurencyjna, baaardzo ciekawa :)

#    if len(c) == 1 : return 0
#    if len(c) == 2: return 0 if c[1]==1 else 1
#    if c[2]==1: 
#        return 1 + jumpingOnClouds(c[1:])
#    if c[2]==0:
#        return 1 + jumpingOnClouds(c[2:])