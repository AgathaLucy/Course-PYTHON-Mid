# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 18:12:12 2020

@author: 9
"""

'''
Do klasy z poprzedniego zadania dodaj 3 metody:

show info, która

    -wyświetli wielkimi literami nazwę produktu

    -wyświetli informację o smaku

    -jeśli produkt ma jakieś dodatki to je wyświetli

    -jeśli produkt ma nadzienie to je wyświetli
    (oczywiście przetestuj działanie funkcji po jej zaimplementowaniu)

set_filling, która

    -jako argument przyjmie nazwę nadzienia ciasta

    -zapisze ją w atrybucie filling dla ciasta

    -(oczywiście przetestuj działanie funkcji)

add_additives, która

    -jako argument przyjmie listę dodatków

    -wartości z listy doda do aktualnej listy dodatków
    (tę funkcję też przetestuj)

Następnie dodaj do muffinki nadzienie kremowe, a do bezy dodaj kokos i posypkę 
kakaową. Tak zmodyfikowane wypieki wyświetl. Poniżej zobacz spodziewany efekt:

Today in our offer:
VANILLA CAKE
Kind:    cake
Taste:   vanilla
Additives:
	chocolade
	nuts
Filling: cream
--------------------
CHOCOLADE MUFFIN
Kind:    muffin
Taste:   chocolade
Additives:
	chocolade
Filling: vanilla cream
--------------------
SUPER SWEET MARINGUE
Kind:    meringue
Taste:   very sweet
Additives:
	cocoa powder
	coconuts
--------------------
'''

class Cake:
    
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
    
    
    def showInfo(self):
        print("Name:    {}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
                
        if self.addictions:
            print("Addictions:")
            for a in self.addictions:
                print("\t-{}".format(a))
        
        if self.filling:
            print("Filling: {}".format(self.filling))
        print(30*"-")
        
    
    def set_filling(self, filling):
        self.filling = filling
        
    
    def add_additives(self, addictions):
        self.addictions.extend(addictions)
        
        
cake_01 = Cake("Lemon Curt", "ciasto", "cytrynowy", ["beza"], "")
cake_02 = Cake("Tort Urodzinowy", "tort", "kawowy", ["beza", "kolorowa posypka"], "masa budyniowa")

cake_01.showInfo()
cake_02.showInfo()

cake_01.set_filling("masa cytrynowa")
cake_02.add_additives(["kofeina","małże","Cos na kolorowe i przyjemne sny"])

cake_01.showInfo()
cake_02.showInfo()