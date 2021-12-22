# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:29:30 2020

@author: 9
"""

'''
Budujesz moduł generujący wykresy. Chcesz samodzielnie wpływać na to, jakie 
kolory będą wykorzystane na wykresie. Definiujesz na początku listę kolorów:

["red", "orange", "green", "violet", "blue", "yellow"]

Czasami na wykresie będą prezentowane tylko 3 kategorie i wtedy chcesz 
wykorzystać tylko 3 pierwsze kolory, innym razem wykres ma mieć 5 kategorii 
i potrzebujesz listę 5 kolorów.

Napisz funkcję, która przyjmuje dwa argumenty: listę kolorów i liczbę n. 
Funkcja ma zwracać nową kopię listy kolorów o długości n korzystając z 
przekazanej listy argumentów.


Napisz pętlę, która wygeneruje wszystkie możliwe zestawy kolorów dostępne 
w liście. Pętla powinna radzić sobie z wyświetleniem wszystkich zestawów, 
nawet jeżeli do początkowej listy zostanie kiedyś dodany następny kolor (nie 
korzystaj z wpisywania na stałe wartości liczbowej).
'''

#Zaimportowanie potrzebnym funkcji
from math import factorial
from random import shuffle 

colors=["red", "orange", "green", "violet", "blue", "yellow"]

#definicja funkcji przycinającej listę wejciową
def cutList(list,num):    
    outList=list[:num]
    return outList

#Przypisanie wartoci zmiennej num, odpowiadającej za liczbę kolorów w liscie roboczej
num=''

#Pętla while z blokiem try/except odpowiadają za wprowadzenie odpowiedniego typu zmiennej
while True:
    try:
        num=int(input('How many colors I must used?(you can chose from 1 to {}) '.format(len(colors))))
        break
    except:
        print("ERROR: Your argument must be integer!!!")

#Wywołanie funki cutList i stworzenie listy roboczje
chosen_colors=cutList(colors, num)


newList=chosen_colors[:]

#Utworzenie listy zbiorczej wszytkich kombinajci kolorów
mainList=[]

#Pętla while działa dopuki, dopóki mainList nie ma wszytkich możliwych kombinajci kolorów
while len(mainList)<factorial(num):
#    Dodanie newList do mainList 
    mainList.append(newList[:])
#    Przetasowanie elementów w newList
    shuffle(newList)
    
    while newList in mainList:
#       Losuj dopuki nie wylosujesz nie istniejącej jeszcze w liscie głównej kombinacji
        shuffle(newList)
#        Jeżeli lista mainList ma już wszytkie kombinajce przerwij działanie
        if len(mainList)==factorial(num):
            break

#Wydrukuj mainList
print(mainList)


#Drugie zadanie
'''
Napis też można "kroić". Wytnij z poniższego tekstu pochodzącego z 
https://nonsa.pl/wiki/Korporacja (dawniej nonsensopedia.pl) fragment tłumaczący 
pochodzenie słowa "Korporacja" - fragment znajduje się w nawiasach 
(same nawiasy pomiń):
'''
    
text='''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) –\ 
organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym \
światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych.\ 
W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do \
wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.
'''
newText=text[text.index('(')+1:]
newText=newText[:newText.index(')')]
print('Korporacja',newText)
