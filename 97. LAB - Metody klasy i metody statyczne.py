# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:34:34 2020

@author: 9
"""
'''
Dlaczego warto wykonywać zadania? Bo w tym zadaniu będzie ciekawie. Skorzystasz
 z 2 fantastycznych funkcji, których nie omówiłem na kursie. Ale po kolei:

Naszym zadaniem jest zapisanie na dysku informacji o wyrobach naszej cukierni. 
Obiekty klasy Cake są już trochę skomplikowane, wiec do ich eksportowania na 
dysk i importowania z dysku wykorzystamy moduł pickle. (Kilka słów o module i 
link do dokumentacji znajdziesz poniżej), a tu krótkie streszczenie:

Moduł zaimportujesz komendą

import pickle

Jeśli f to uchwyt do pliku, a obj to jakiś obiekt, to możesz go zapisać na 
dysku poleceniem:

pickle.dump(obj, f)

A jeśli potem ten obiekt chcesz odczytać, to możesz to zrobić tak:

new_obj = pickle.load(f)



No to do roboty.

Dodaj do klasy funkcję save_to_file. Funkcja ma pracować na poziomie instancji

Funkcja ma przyjąć argument path wskazujący na ścieżkę dostępu do pliku

Plik należy otworzyć do zapisu w trybie binarnym i korzystając z pikle.dump 
zapisać bieżący obiekt do pliku

Przetestuj działanie funkcji zapisując cake01 i cake02 do plików. Nadaj plikom 
rozszerzenie bakery



Dodaj do klasy funkcję read_from_file. Funkcja ma przyjmować jako argument 
ścieżkę do pliku

Funkcja ma otworzyć plik na odczyt w trybie binarnym i wczytać obiekt klasy 
Cake z tego pliku korzystając z pickle.load

Nowy obiekt należy dopisać do zmiennej klasy bakery_offer i zwrócić ten obiekt

Przetestuj działanie funkcji wczytując plik z poprzedniego przykłądu do nowego 
obiektu np. cake05. Aby przetestować czy wszystko się udało wywołaj dla tego 
nowego obiektu z funkcji show_info



No dobrze, ale jeśli znamy ścieżkę dostępu do katalogu i  w tym katalogu 
znajdują się pliki z rozszerzeniem bakery, to chcielibyśmy mieć funkcję , 
która zwróci listę takich plików. Odpowiednią do tego prawie gotową funkcję 
znajdziesz w module glob:

import glob

Aby otrzymać listę plików z rozszerzeniem txt z katalogu c:/temp możesz wywołać
funkcję:

glob.glob('c:/temp/*.txt')



Dodaj do klasy Cake funkcję statyczną get_bakery_files, która jako argument 
przyjmie nazwę katalogu

Funkcja ma zwrócić listę plików z rozszerzeniem bakery z przekazanego 
argumentem katalogu

Przetestuj działanie funkcji



-----------------------------------------------------------------------------------

Krótka dokumentacja modułu pickle ze strony:

https://pl.python.org/docs/tut/node9.html

7.2.2 Moduł pickle

Napisy mogą być w łatwy sposób zapisywane i czytane z pliku. Liczby wymagają 
trochę więcej zachodu, bowiem metoda read() zwraca tylko napis, który musi być 
poddany działaniu takiej funkcji,, jak string.atoi(), która pobiera napis w 
rodzaju '123' i zwraca wartość liczbową 123. W przypadku jednak, gdy chce się 
przechowywać w pliku bardziej złożone typy danych jak listy, słowniki lub 
instancje klas, sprawy się nieco komplikują.

Python dostarcza standardowy moduł pickle, który zaoszczędza użytkownikom 
pisania i śledzenia kodu służącego do zachowywania skomplikowanych typów 
danych. Ten zadziwiający
7.4. moduł potrafi wziąć na wejściu prawie każdy obiekt Pythona (nawet pewne 
formy kodu!) i przekształcić go w napis. Proces ten zwie się marynowaniem
7.5. Rekonstruowanie obiektu z formy napisowej zwie się odmarynowaniem
7.6. Pomiędzy marynowaniem a odmarynowaniem, napis reprezentujący obiekt może 
zostać zapisany w pliku lub w innej danej, lub przesłany połączeniem sieciowym 
do jakiegoś oddalonego komputera.
7.7 Jeżeli istnieje obiekt x i obiekt pliku f, który został otwarty do pisania, 
to najprostszy sposób zamarynowania obiektu zajmuje jeden wiersz kodu:

pickle.dump(x, f)

Zakładając, że f jest obiektem pliku, który został otwarty do czytania, 
odmarynowanie przebiega następująco:
    
x = pickle.load(f)

(Istnieją warianty tego mechanizmu użyteczne w przypadku marynowania wielu 
obiektów, lub gdy nie chce się zapisać danych marynaty w pliku -- skonsultuj 
się z pełną dokumentacją dla modułu pickle, którą znajdziesz w 
«Opisie biblioteki»).

pickle jest standardowym sposobem na uczynienie obiektów Pythona trwałymi 
i ponownie użytymi przez inne programy lub przyszłe wywołania tego samego 
programu: technicznym określeniem tego mechanizmu jest trwałośćobiektu. 
Z powodu powszechnego użycia modułu pickle, wielu autorów piszących 
rozszerzenia do Pythona, dba o to, aby nowe typy danych, takie jak macierze, 
mogły być poprawnie zamarynowane i odmarynowane.



--------------------------------------------------------------------------------------------------

https://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie/Praca_z_katalogami

Jest jeszcze inna metoda dostania się do zawartości katalogu. Metoda ta jest 
bardzo potężna i używa zestawu symboli wieloznacznych (ang. wildcard), 
z którymi można się spotkać pracując w linii poleceń.

>>> os.listdir("c:\\music\\_singles\\")               #(1)
['a_time_long_forgotten_con.mp3', 'hellraiser.mp3',
'kairo.mp3', 'long_way_home1.mp3', 'sidewinder.mp3',
'spinning.mp3']

Jak wcześniej powiedzieliśmy, os.listdir pobiera ścieżkę do katalogu i zwraca 
wszystkie pliki i podkatalogi, które się w nim znajdują.

Z drugiej strony, moduł glob na podstawie podanego wyrażenia składającego się 
z symboli wieloznacznych, zwraca pełne ścieżki wszystkich plików, które 
spełniają te wyrażenie. Tutaj wyrażenie jest ścieżką do katalogu plus "*.mp3", 
który będzie dopasowywał wszystkie pliki .mp3. Dodajmy, że każdy element 
zwracanej listy jest już pełną ścieżką do pliku.

>>> import glob
>>> glob.glob('c:\\music\\_singles\\*.mp3')           #(2)
['c:\\music\\_singles\\a_time_long_forgotten_con.mp3',
'c:\\music\\_singles\\hellraiser.mp3',
'c:\\music\\_singles\\kairo.mp3',
'c:\\music\\_singles\\long_way_home1.mp3',
'c:\\music\\_singles\\sidewinder.mp3',
'c:\\music\\_singles\\spinning.mp3']

Jeśli chcemy znaleźć wszystkie pliki w określonym katalogu, gdzie nazwa zaczyna
się od "s", a kończy na ".mp3", możemy to zrobić w ten sposób.

>>> glob.glob('c:\\music\\_singles\\s*.mp3')          #(3)
['c:\\music\\_singles\\sidewinder.mp3',
'c:\\music\\_singles\\spinning.mp3']

Teraz rozważ taki scenariusz: mamy katalog z muzyką z kilkoma podkatalogami, 
wewnątrz których są pliki .mp3. Możemy pobrać listę wszystkich tych plików za 
pomocą jednego wywołania glob, wykorzystując połączenie dwóch wyrażeń. 
Pierwszym jest "*.mp3" (wyszukuje pliki .mp3), a drugim są same w sobie ścieżki
do katalogów, aby przetworzyć każdy podkatalog w c:\music. Ta prosto 
wyglądająca funkcja daje nam niesamowite możliwości!

>>> glob.glob('c:\\music\\*\\*.mp3')                  #(4)
'''
import pickle
import glob

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
    
    
    def SaveToFile(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)
    
    @classmethod
    def ReadFromFile(cls,path):
        with open(path, 'rb') as f:
            nCiasto = pickle.load(f)
                    
        cls.bakery_offer.append(nCiasto)    
        
        return nCiasto
    
    @staticmethod
    def GetBakeryFiles(catalog):
        return glob.glob(catalog+'*.bakery')
    
    
    def __getText(self):
        return self.__text
    
    
    def __setText(self, newText):
        if self.kind == "ciasto":
            self.__text = newText
    
    
    Text = property(__getText, __setText, None, "")
    
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

path = 'E:/WszytkieProjekty/Cwiczeniea Python/PythonPozniomZaawansowany/'

cake_01 = Cake("Lemon Curt", 'ciasto', "cytrynowy", ["beza"], "", False,"Sto lat Mateusz!")
cake_02 = Cake("Tort Urodzinowy", "tort", "kawowy", ["beza", "kolorowa posypka"], "masa budyniowa",False,"")

cake_01.SaveToFile(path+'cake-0{}.bakery'.format('1'))
cake_02.SaveToFile(path+'cake-0{}.bakery'.format('2'))


print(Cake.GetBakeryFiles(path))