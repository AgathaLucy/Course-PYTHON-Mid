# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:10:58 2020

@author: 9
"""

line = input("Podaj zdanie lub słowo a ja sprawdzę czy to palindrom: ")
reversLine=line.replace(" ","").lower()[::-1]

if line.lower() == reversLine:
    print("'{}' jest palindromem.".format(line))
else:
    print("Podana fraza nie jest palindromem :\(")