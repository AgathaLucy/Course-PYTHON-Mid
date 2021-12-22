# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 04:30:50 2020

@author: 9
"""
#definicja ma przyjmować ilosć skarpetek i ich nie sparowaną listę np.[1,2,4,3,1,2]
#i zwracać ilosc par w zbiorze

def sockMerchant(n, ar):
    dict={}
    pair=0

    for a in ar:
        if a in dict:
            dict[a]+=1
        else:
            dict[a]=1
    for key in dict:
        pair+=dict[key]//2
    
    return pair


ar=[9,1,2,1,2,9,1,1,2,4,5,5,]


print(sockMerchant(12,ar))
