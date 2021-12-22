# -*- coding: utf-8 -*-
"""
Created on Mon May 18 03:05:25 2020

@author: 9
"""
'''
Oto uproszczona klasa Cake:

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
 
    @property
    def full_name(self):
       
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


Dodaj dokumentację:

do klasy

do metody __init__

do właściwości full_name

Wyświetl help na temat klasy oraz na temat właściwości full_name
'''

class Cake:
    """
    Klasa Cake reprezentu wyroby cukiernicze
    """
 
    bakery_offer = []
    """
    lista oferowanych przez zakład wyrobów cukierniczych
    """
 
    def __init__(self, name, kind, taste, additives, filling):
        """
        name - zmienna typu str, reprezentuje nazwę danego wypieku
        kind - zmienna typu str, reprezentuje rodzaj (tort, biszkopt itp.) wypieku
        taste - zmienna typu str, reprezentuje główny smak wypieku
        additives - zmienna typu str, reprezentuje dadatki (np. koloroawa posypka)
        filling - zmienna typu str, reprezentuje wypełnienie/masa  wypieku
        """
               
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
 
    @property
    def full_name(self):
        """
        wlaciwocs full_name zwraca na pełną nazwę wypieku w postaci: --== nazwa  - rodzaj ==--
        """
       
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)

help(Cake)
help(Cake.full_name)