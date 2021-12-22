# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:20:53 2020

@author: 9
"""
'''
W tym zadaniu nadal pracujemy nad klasą "Ciastko"

Dodaj do klasy Cake ukryty atrybut gluten_free. (To jedna z ważniejszych 
informacji o wypiekach, dlatego staramy się, żeby ten atrybut można było 
ustawić tylko raz podczas tworzenia obiektu, dzięki czemu później podczas 
pracy programu nie zmienimy przypadkowo wartości w tym polu)

Zmień funkcję __init__ oraz show_info tak, aby obsługiwały nowy atrybut klasy

Tworząc nowe obiekty wypieków przekazuj wartość True lub False wskazującą na 
to czy wypiek jest bezglutenowy (o ile wiem jajka nie zawierają glutenu, więc 
bezy są bezglutenowe)

Przetestuj działanie programu

Spróbuj w kodzie programu (np. po wyświetleniu oferty ciastkarni) zmienić 
atrybut __gluten_free

Czy po uruchomieniu masz błąd? Dlaczego? Korzystając z polecenia dir(cake03) 
zobacz jakie atrybuty ma ten obiekt

Zmień wartość atrybutu korzystając ze specjalnie i automatycznie utworzonego 
atrybutu o specyficznej budowie tak, jak to było zrobione w materiale video

Wyświetl ponownie informacje o cake03 (beza) - czy teraz stała się wyrobem 
glutenowym?
'''
class Cake:
    
    known_kinds=['ciato', 'muffina', 'beza', 'biszkop', 'eklerk', 'swiateczne', 'pretcel','inne']
    bakery_offer=[]
    
    
    def __init__(self, name, kind, taste, addictions, filling, glutenFree):
        
        self.name = name
        if kind in Cake.known_kinds:
            self.kind = kind
        else:
            self.kind = 'inne'
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.__glutenFree = glutenFree
        Cake.bakery_offer.append(self)
    
    
    def showInfo(self):
        print("Nazwa:    {}".format(self.name.upper()))
        print("Rodzaj:   {}".format(self.kind))
        print("Smak:     {}".format(self.taste))
                
        if self.addictions:
            print("Dodatki:")
            for a in self.addictions:
                print("\t  -{}".format(a))
        
        if self.filling:
            print("Wypełnienie: {}".format(self.filling))
        print('Wolne od glutenu: {}'.format(self.__glutenFree))
        print(30*"-")
        
    
    def set_filling(self, filling):
        self.filling = filling
        
    
    def add_additives(self, addictions):
        self.addictions.extend(addictions)
    
cake_01 = Cake("Lemon Curt", "ciasto", "cytrynowy", ["beza"], "", False)
cake_02 = Cake("Tort Urodzinowy", "tort", "kawowy", ["beza", "kolorowa posypka"], "masa budyniowa",False)
cake_03 = Cake('Bezy','beza','bezy',[],[],True)
cake_04 = Cake('wafle kakaowe','wafle','kakaowy',[],'kakao', False)

for c in Cake.bakery_offer:
    c.showInfo()
    
cake_03.__glutenFree=True

print(dir(cake_03))

cake_03._Cake__glutenFree = False

cake_03.showInfo()