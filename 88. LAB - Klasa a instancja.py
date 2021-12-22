# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:08:42 2020

@author: 9
"""

'''
Pracujemy z wynikiem LAB z poprzedniej lekcji.

Dodaj do klasy Cake atrybut na poziomie klasy. Nazwij go known_types. Będą w 
nim przechowywane produkowane w naszej cukierni słodkości. Przypisz do zmiennej
listę np. w następującej postaci:

['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']

Zmień __init__ tak, że jeżeli jako parametr kind zostanie przekazana wartość 
znajdująca się na liście known_kinds, to zostanie zaakceptowana, ale jeśli ktoś
przekaże wartość spoza tej listy, to do nowo tworzonego obiektu do atrybutu 
kind zostanie wpisany napis other.

Przetestuj działanie nowej funkcji __init__ tworząc obiekt "wafel kakaowy":

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')



Dodaj do klasy Cake nowy atrybut bakery_offer, który na początku będzie pustą 
listą.

Zmień __init__ tak, aby po utworzeniu nowego obiektu typu Cake, został on 
automatycznie dodany do listy bakery_offer

Usuń ze skryptu niepotrzebne już instrukcje tworzące listę bakery_offer 
i dodające obiekty tej klasy do tej listy.

Zmień pętlę wyświetlającą informację o ofercie cukierni tak, aby korzystała 
z atrybutu klasy (względem zadania z labu 82)



Sprawdź czy obiekty cake01 i inne są instancjami klasy Cake korzystając 
z funkcji isinstance i type

Wyświetl informacje o instancji cake01 i o klasie Cake korzystając 
z funkcji vars i dir
'''



class Cake:
    
    known_kinds=['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer=[]
    
    
    def __init__(self, name, kind, taste, addictions, filling):
        
        self.name = name
        if kind in Cake.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        Cake.bakery_offer.append(self)
    
    
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

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

cake04.showInfo()

for c in Cake.bakery_offer:
    c.showInfo()
    
print(isinstance(cake_01, Cake))
print(type(cake_01) is Cake)

print(vars(Cake))
print(vars(cake_01))

print(dir(Cake))
print(dir(cake_01))
