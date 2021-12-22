# -*- coding: utf-8 -*-
"""
Created on Sat May  2 01:50:50 2020

@author: 9
"""
'''
W tym LAB pracujemy z klasą z poprzedniej lekcji (jeśli nie masz rozwiązania 
skopiuj sobie moją propozycję rozwiązania z poprzedniej lekcji)

Do klasy należy dodać atrybut ukryty __text. Odpowiada on za napis umieszczony
na torcie.


W funkcji __init__ przyjmij nowy argument text

Zapisz go w zmiennej __text przeprowadzając kontrolę: 
    napis można zapisać w instancji tylko jeżeli kind jest 'cake' lub text jest
    napisem pustym. Jeśli te warunki nie są spełnione wyświetl diagnostyczny 
    komunikat (print dla Ciebie, żeby było wiadomo co się dzieje)

Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text

Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text 
i zaktualizuje atrybut __text tylko dla wyrobów z kind 'cake'

Zdefiniuj właściwość Text korzystającą z powyższych funkcji.

Tworząc obiekty klasy Cake przekaż dodatkowy argument text - umieść napisy 
puste lub inne typowo  "tortowe", część poprawnych (czyli napis na torcie) 
i część niepoprawnych (np. napis na waflu)

Wyświetl wszystkie informacje o wszystkich wypiekach

Spróbuj wstawić do właściwości Text napis na torcie i na innym wypieku 
nietortowym - prześledź poprawność tych operacji ponownie wyświetlając ofertę 
cukierni
'''
class Cake:
    
    known_kinds=['ciasto', 'muffina', 'beza', 'biszkop', 'eklerk', 'swiateczne', 'pretcel','inne']
    bakery_offer=[]
    
    
    def __init__(self, name, kind, taste, addictions, filling, glutenFree, text):        
        self.name = name
        if kind in Cake.known_kinds:
            self.kind = kind
        else:
            self.kind = 'inne'
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.__glutenFree = glutenFree
        if self.kind =='ciasto' or text=="":
            self.__text = text
        else:
            print('W danym rodzaju wyrobów cukierniczych nie jest możliwe wprowadzenie opisu. ')
        Cake.bakery_offer.append(self)
    
    def __getText(self):
        return self.__text
    
    def __setText(self, newText):
        if self.kind == "ciasto":
            self.__text = newText
    
    Text = property(__getText, __setText, None,"")
    
    def showInfo(self):
        print("Nazwa:    {}".format(self.name.upper()))
        print("Rodzaj:   {}".format(self.kind))
        print("Smak:     {}".format(self.taste))
        if self.kind =='ciasto':
            print("Tekst:    {}".format(self.__text))        
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
        

cake_01 = Cake("Lemon Curt", 'ciasto', "cytrynowy", ["beza"], "", False,"Sto lat Mateusz!")
cake_02 = Cake("Tort Urodzinowy", "tort", "kawowy", ["beza", "kolorowa posypka"], "masa budyniowa",False,"")
cake_03 = Cake('Bezy','beza','bezy',[],[],True,"")
#cake_04 = Cake('wafle kakaowe','wafle','kakaowy',[],'kakao', False,"")


for c in Cake.bakery_offer:
    c.showInfo()

cake_01.Text="zmiana"
cake_03.Text="zmiana"

for c in Cake.bakery_offer:
    c.showInfo()