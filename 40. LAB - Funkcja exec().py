# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:26:17 2020

@author: 9
"""
'''
Tym razem pracujesz w zwariowanym ośrodku badawczym...

Profesorowie przygotowują swoje skrypty i umieszczają je w określonym katalogu.
Twój skrypt ma za zadanie przeczytać te skrypty i je po kolei wykonywać.

Poniżej znajdują się dwa przykładowe skrypty. Każdy z nich skopiuj i zapisz w 
osobnym pliku (jeżeli wykonanie skryptu miało by być zbyt długie, możesz 
zmienić ilość iteracji w zmiennej for, ale nie powinno być tak źle):

import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(math.sin(x) * x**2))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))


import math
 
argument_list = []
results_list = []
 
for i in range (1000000):
    argument_list.append(i/10)
    
for x in argument_list:
    results_list.append(abs(x**3 - x**0.5))
 
print('min = {}  max = {}'.format(min(results_list), max(results_list)))

Utwórz listę zawierającą ścieżki dostępu do skryptów:

files_to_process = [
    r"C:\Python\math_sin_square.py",
    r"C:\Python\math_square_root.py"
    ]
Dla każdego pliku:

wyświetl nazwę pliku (skorzystaj z funkcji os.path.basename z modułu os)

otwórz dany plik i wczytaj go do zmiennej source

Wykonaj ten skrypt
'''

import os
#Lista scieżek do plików
files_to_process = [
    r"E:\WszytkieProjekty\Cwiczeniea Python\PythonPozniomZaawansowany\math_sin_square.py",
    r"E:\WszytkieProjekty\Cwiczeniea Python\PythonPozniomZaawansowany\math_square_root.py"
    ]

for file in files_to_process:

    #Otworzenie danego pliku 
    with open(file, 'r') as source:
        #Wyswietlenie nazwy pliku
        print("Uruchomiono plik: {}...".format(os.path.basename(file)))
        #Wczytanie zawartosci pliku
        content = source.read()
        #Wykonanie kodu z pliku
        exec(content)




