# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 22:06:01 2020

@author: 9
"""

'''
Oto deklaracja zmiennej days:

days = ['mon','tue','wed','thu','fri','sat','sun']

należy utworzyć zmienną workdays, która początkowo będzie zawierać te same 
elementy co days

następnie należy usunąć z workdays dni wolne

na koniec wyświetl days i workdays i upewnij się, że sobota i niedziela 
zniknęły tylko z listy workdays
'''

days = ['mon','tue','wed','thu','fri','sat','sun']
workdays=days.copy()
workdays=workdays[:-2]
print(days,"\n",workdays)
print(id(days),id(workdays))