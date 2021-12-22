# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:40:33 2020

@author: 9
"""
'''
W tym zadaniu zbudujesz proces służący do budowy łańcucha transformacji danych 
liczbowych.

1. Utwórz w swoim skrypcie następujące funkcje:

def double(x):
    return 2 *x
 
def root(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2
2. Zdefiniuj liczbę number o wartości 8

3. Zdefiniuj listę transformations składającą sie z funkcji:

double

root

div2

negative

4. Do tymczasowej zmiennej tmp_return_value wpisz wartość number

5. Napisz pętlę, która:

przejdzie przez wszystkie pozycje listy transformations

za każdym razem wywoła odpowiednią funkcję, przekazując do niej aktualną 
wartość argumentu tmp_return_value

wyświetli aktualną wartość zmiennej tmp_return_value

6. Przetestuj działanie skryptu również dla listy transformacji z operacjami:

root

root

div2

double
'''

def double(x):
    return 2 *x
 
def root(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

number=8

transformations=[double, root, negative, div2]

tmp_return_value=number

for tf in transformations:
    print(tf(tmp_return_value))


transformations=[root, root, div2, double]

#6. punkt
for tf in transformations:
    print(tf(tmp_return_value))

#Zadania z kursu    
'''
def double(x):
    return 2 *x
 
def root(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2
 
number = 8
transformations = [double, root, div2, negative]
 
print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
 
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))
 
number = 125
transformations = [root, root, div2, double]
      
print('Starting transformations')
tmp_return_value = number
for transformation in transformations:
 
    tmp_return_value = transformation(tmp_return_value)
    print('{}: temporal result is {}'.format(transformation.__name__, tmp_return_value))
'''