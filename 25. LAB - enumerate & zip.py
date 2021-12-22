# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 00:01:58 2020

@author: 9
"""
'''
Utwórz następujące listy:

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
Korzystając ze "sprytnej" metody pracy z for wyświetl komunikaty w postaci:

The leader of "...nazwa projektu..." is ...imię i nazwisko lidera...
'''


projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for leader, project in zip(leaders,projects):
    print("The leader of {} is {}.".format(project,leader))

'''
Utwórz kolejną listę z datami rozpoczęcia projektów:

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

The leader of "...nazwa projektu..."  started ...data rozpoczęcia projektu... 
is ...imię i nazwisko lidera...
'''
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, leader, date  in zip(projects,leaders,dates):
    print("The leader of {} is {} started {}.".format(project,leader,date))

'''
Korzystając ze "sprytnego" złożenia enumerate i zip - dodaj do komunikatu 
dodatkowo numer kolejny projektu rozpoczynając od 1:

...numer kolejny... - The leader of "...nazwa projektu..."  started ...
data rozpoczęcia projektu... is ...imię i nazwisko lidera...
'''

for pos, (project, leader, date)  in enumerate(zip(projects,leaders,dates)):
    print("{}. The leader of {} is {} started {}.".format(pos+1,project,leader,date))


