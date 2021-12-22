# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 02:11:46 2020

@author: 9
"""
'''
Piszesz program, który będzie obsługiwał wpłatomat. To będzie super nowoczesny 
wpłatomat, do którego można też wpłacać monety. Ilekroć ktoś wpłaca pieniądze 
należy policzyć ile banknotów lub monet danego nominału znajduje się w kasie.

Zacznij od poniższej listy, która definiuje dostępne nominały

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

Dowolną metodą utwórz słownik, który jako klucz będzie przechowywał wartość 
nominału, a jeśli chodzi o wartości słownika, to póki co mają być zerowe. 
Proponuję nazwać ten słownik dict_denominations.

Teraz do bankomatu podchodzą klienci i wpłacają:

dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

Napisz polecenie for, które wyświetli ile mamy pieniędzy w określonych monetach
lub banknotach. Zestawienie ma zacząć sie od najmniejszych nominałów, 
a skończyć na największych. Jeśli masz ochotę, to zadbaj o ładne formatowanie 
wyniku:

-nominał na 6 znakach, w tym 2 po przecinku

-ilość monet/banknotów - liczba całkowita maksymalnie 5-cyfrowa

możesz skorzystać z artykułu: 
https://www.python-course.eu/python3_formatted_output.php 
(skocz do części dot. polecenia format - jeśli link nie byłby aktualny daj znać
 w Q&A - z góry dzięki!)



Oto przykładowy output:

Denominate:   0.01 - amount     0
Denominate:   0.02 - amount     0
Denominate:   0.05 - amount     0
Denominate:   0.10 - amount     0
Denominate:   0.20 - amount     0
Denominate:   0.50 - amount     1
Denominate:   1.00 - amount     0
Denominate:   2.00 - amount     3
Denominate:   5.00 - amount     2
Denominate:  10.00 - amount     0
Denominate:  20.00 - amount     3
Denominate:  50.00 - amount     2
Denominate: 100.00 - amount     2
Denominate: 200.00 - amount     0
Denominate: 500.00 - amount     0
'''
#lista zawierająca nominały
banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

#deklaracja słownika
dict_denominations={}

#ustanowienie kluczy i ich wartosci początkowych
for key in banknotes_coins:
    dict_denominations[key]=0

#wpłacone pieniądze
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1
 
dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2
 
dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

#wyswietlenie stanu wpłatomatu
for key in dict_denominations:
    print("Denominate:{0:6.2f} - amount{1:6d}".format(key,dict_denominations[key]))