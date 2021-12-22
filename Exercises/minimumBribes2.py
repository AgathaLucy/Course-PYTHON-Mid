# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:26:14 2020

@author: 9
"""

q=[5, 1, 2, 3, 7, 8, 6, 4]

def minimumBribes(Q):

    moves = 0 

    for P in Q:
        
        if P - (Q.index(P)+1) > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1,0),Q.index(P)):
            if Q[j] > P:
                moves += 1
    
    print(moves)
    
print(minimumBribes(q))
