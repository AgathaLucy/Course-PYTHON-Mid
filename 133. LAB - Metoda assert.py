# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:39:08 2020

@author: 9
"""
'''
Oto klasa z poprzedniego laboratorium:

import datetime as dt
 
class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
 
    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")
 
    @classmethod
    def publish_offer(cls, trips):
 
        list_of_errors = []
 
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
        
        if len(list_of_errors) > 0:
            raise Exception("The list of trips has errors: {}".format(list_of_errors))
        else:
            print('the offer will be published...')
         
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]
 
try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')

Zmień testy wykonywane w funkcji check_data tak, aby wykorzystywały assert.

Zamień instrukcję if/else z  metody publish_offer na assert

A teraz się zastanów... czy ZAWSZE należy stosować polecenie assert zamiast 
if/else? Co stałoby się z Twoim programem jeśli uruchomisz go w środowisku, 
w którym PYTHONOPTIMIZE jest ustawione na TRUE ? Sprawdź to i udziel odpowiedzi!
'''

import datetime as dt

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end
    
    def check_data(self):
        assert len(self.title) > 0, "Nazwa wycieczki jest pusta!"
        assert self.start <= self.end, "Data rozpoczęcia wycieczki jest później niż jej zakończenia!"
    
    @classmethod
    def publish_offer(cls, trips):
        
        list_of_errors = []
        
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}:{}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}:{}".format(trip.symbol, str(e)))
        
        assert len(list_of_errors) == 0, "Lista wycieczek zawiera błędy {}!!".format(list_of_errors)
        print('the offer will be published...')

   
trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]

try:
    print("Sprawdzam wycieczki...")
    Trip.publish_offer(trips)
    print("...zakończono.")
except Exception as e:
    print("Napotkano błędy...")
    print(e)
    print("Popraw błędy")      


#W środowisku, w którym PYTHONOPTIMIZE jest ustawione na TRUE, działanie 
#programu opartego o metodę assert będzie wadliwe, lub nie wykona się w cale.
#Nie zawsze powinno się używać metody assert, albo opierać o nią funkcjonowanie 
#programu. Jak ze wszystki trzeba zachwoać umiar.
    
#Niestety. Assert sprawdza się świetnie przy identyfikowaniu błędów związanych 
#typowo z kodem aplikacji. Takie testy wystarcza uruchamiać w środowisku 
#TST/DEV.  Kiedy aplikacja przechodzi do środowiska produkcyjnego uruchamianie 
#tych testów jest zbyteczne.
    
#Jeśli jednak spodziewamy się błędów związanych z danymi, to takie testy 
#powinny być wykonywane ZAWSZE, niezależnie od środowiska.  W tym przypadku 
#lepiej sprawdzi się if/else i raise.