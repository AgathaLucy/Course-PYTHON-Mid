# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 07:32:38 2020

@author: 9
"""

def repeatedString(s, n):
    
    m=n//len(s)
    x=n%len(s)
    numX=s[:x].count("a")
    num=s.count("a")*m
    numA=num+numX
#    numA = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    return numA

s="adb"
print(repeatedString(s, 1000000000000))

#Mniej lini
#s, n = input().strip(), int(input().strip())
#print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))