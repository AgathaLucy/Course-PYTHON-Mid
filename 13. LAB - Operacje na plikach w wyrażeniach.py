# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:08:59 2020

@author: 9
"""

'''
Utwórz plik i wpisz do niego kilka słów, np co widzisz za oknem :)

Utwórz funkcję, która jako parametr przyjmuje ścieżkę dostępu do pliku i zwraca
ilość słów w tym pliku, jeśli potrzebujesz kroków pomocniczych oto i one:

Otwórz plik poleceniem open (możesz skorzystać z parametru encoding="utf-16" 
jeżeli trzeba)

Wczytaj plik do zmiennej korzystając z funkcji read()

"Rozbij" wczytaną zawartość korzystając z funkcji split()

Policz ile elementów jest zwracanych przez funkcję split()

Zwróć tą wartość

W głównym skrypcie:

zadeklaruj zmienną path i przypisz jej wartość wskazującą na plik utworzony 
na początku

napisz polecenie warunkowe, które sprawdzi czy plik istnieje

jeśli tak, wywoła funkcję, policzy ilość słów w pliku i wyświetli o tym 
informację

napisz wyrażenie logiczne, które wykona te same czynności, co wcześniej 
napisana instrukcja if
'''

import os

def wordsCounter(path):
    file=open(path)
    words=file.read()
    #mogłem połączyć poniższe dwie linijki w jedną:
    #numberOfWords=len(words.split(' '))
    words=words.split(' ')
    numberOfWords=len(words)
    file.close()
    return numberOfWords

path=r'E:\WszytkieProjekty\Cwiczeniea Python\PythonPozniomZaawansowany\text.txt'

if os.path.isfile(path):
    print("W danym pliku jest:",wordsCounter(path),"słów.")
 
result= os.path.isfile(path) and wordsCounter(path)
print(result)

#Przykład z kursu
#
#def CountWords(path):
#    with open(path,'r', encoding='utf-16') as f:
#        content = f.read()
#        word_count = len(content.split())
#    return word_count
# 
# 
#path = r'c:\temp\test.txt'
#if os.path.isfile(path):
#    print("There are {} words in the file {}".format(CountWords(path), path))
# 
# 
#os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))













