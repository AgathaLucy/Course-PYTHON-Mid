# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 21:45:22 2020

@author: 9
"""

"""
Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim 
szefem otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz 
portów lotniczych:

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj 
połączenie każdy-z-każdym

2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu

3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do A - wygeneruj 
możliwe połączenia krajowe pomijając takie zdublowane trasy.

4. Policz ilość generowanych połączeń w krokach 1,2,3
"""

ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']
#Zad 1
flightRoute=[(a,b) for a in ports for b in ports]
print("This is list of flight routes: \n{}, \nwe got {} routes in it.".format(flightRoute,len(flightRoute)))
#Zad 2
flightRoute=[(a,b) for a in ports for b in ports if a!=b]
print("This is list of flight routes: \n{}, \nwe got {} routes in it.".format(flightRoute,len(flightRoute)))
#Zad 3
flightRoute=[(a,b) for a in ports for b in ports if a<b]
print("This is list of flight routes: \n{}, \nwe got {} routes in it.".format(flightRoute,len(flightRoute)))

'''
flightRoute=[(a,b) for a in ports for b in ports if a<b]

Porównujemy kody znaków. A<B, B<C, C<D itd.
W przypadku tego zadania chcieliśmy wykluczyć zdublowane połączenia. Jako 
zdublowane połączenie traktujemy z portu A do B i z B do A.  Ten znak ostrej 
nierówności to "sztuczka programistyczna".  Skoro A jest mniejsze od B, to nasz 
wzór wykryje tylko połączenie A do B, ale połączenie B do A pominie, bo B nie 
jest mniejsze od A.
'''