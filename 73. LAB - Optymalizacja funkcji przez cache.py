# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:38:33 2020

@author: 9
"""

'''
Oto przykład niezbyt dobrze napisanej funkcji wyliczającej wartość w ciągu 
Finobacciego:

def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result
    
Funkcja zamiast wyliczać wartości od najmniejszych do największych i korzystać 
z poprzednich wyników do wyznaczenia kolejnych wartości, każdorazowo wyznacza
poprzednie wartości. Zoptymalizuj funkcję metodą cache, (a jak masz ochotę to 
również przepisz funkcję do lepszej postaci)

   - przygotuj funkcję do testu pomiaru czasu

       - zaimportuj moduł time

       - w zmiennej start zapisz aktualny czas

       - napisz pętlę wyliczającą wartość ciągu zaczynając od 1, a kończąc na 
         sensownej na Twoim komputerze wartości, na którą masz cierpliwość 
         doczekać (u mnie to do około 33-37)

       - każdorazowo wyświetl numer iteracji w pętli i różnicę między czasem 
         bieżącym, a czasem ze zmiennej start

       - zapamiętaj czas trwania obliczeń

   - zoptymalizuj funkcję

       - zaimportuj moduł functools

       - oznacz funkcję fib dekoratorem lru_cache z maksymalną ilością 
         pamiętanych wyników 100

       - na końcu skryptu dodaj instrukcję wyświetlającą wynik polecenia 
         cache_info

       - porównaj wyniki
'''
import time
import functools

@functools.lru_cache()
def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result

start = time.time()
print(fib(33))
stop = time.time()
time = stop - start

print("Program works: {} sec.".format(time))

#Kod z kursu
'''
import time
import functools
 
@functools.lru_cache(maxsize=100)
def fib(n):
    
    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result
 
start = time.time()
 
for i in range(34):
    result = fib(i)
    print('{0:2d}  {2:3.2f}'.format(i, result, time.time() - start))
    
print(fib.cache_info())
'''