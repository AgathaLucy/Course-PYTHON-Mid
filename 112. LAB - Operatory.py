# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:29:29 2020

@author: 9
"""

'''
W tym zadaniu dodasz do klasy Cake obsługę operatora:

__iadd__ 

__str__

Zaczynamy od definicji klasy w postaci:

class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
       
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

dodaj metodę pozwalającą na wygodne formatowanie obiektów klasy Cake do postaci 
tekstu. Niech zwracany będzie napis składający się z atrybutów kind, name oraz 
additives

dodaj metodę pozwalającą na dodawanie do klasy napisu. Ten napis ma być 
dołączany jako kolejny element na liście additives

zmodyfikuj powyższą metodę tak, aby możliwe było przekazanie na raz większej 
ilości  dodatków. Wszystkie one mają być dołączone do listy additives.

zmodyfikuje powyższą metodę tak, że jeśli zostanie ona wykorzystana do dodania 
zmiennych innych typów, to wygenerowany zostanie błąd.

przetestuj w/w metody
'''

class Cake:
 
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
 
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
 
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)
 
    def __str__(self):
        return "Rodzaj: {}, nazwa: {}, dodatki: {}".format(self.kind,self.name,self.additives)
    
    def __iadd__(self,other):
        if type(other) == list:
            additives = self.additives
            additives.extend(other)
            return Cake(self.name, self.kind, self.tastem, additives, self.filling)
        elif type(other) == str:
            additives = self.additives
            additives.append(other)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        else:
            print("Podany typ zmiennej {}, nie został zaimplementowany".format(other))
            
            
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')


print(cake01)

cake01 += 'Sto lat'

print(cake01)