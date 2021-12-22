# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 12:06:17 2020

@author: 9
"""

'''
W tym zadaniu należy zapisać na dysku zawartość kilku stron www. Po zakończeniu
pobierania należy wyświetlić komunikat o powodzeniu. Jednak w przypadku błędu 
należy wyświetlić informację o błędzie i przerwać pętlę. Jeśli taki opis Ci 
wystarcza - do działa!

A oto opis "krok po kroku"

zaimportuj moduły os i urllib.request

w zmiennej data_dir zapisz ścieżkę do katalogu, w którym mają być zapisywane 
strony

w zmiennej pages zapisz informacje o stronach do pobrania. Może to być np. 
lista słowników:

pages = [

    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},

    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },

    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]



dla każdej stony z pages:

zapisz w zmiennej path ścieżkę to pliku powstałą z połączenia data_dir, nazwy 
strony pobranej z  pages i ".html"

korzystając z  funkcji:
    
    urllib.request.urlretrieve(<adres strony>, <sciezka do pliku>) 

zapisz stronę na dysku (na tym etapie przetestuj sobie działanie programu)

wewnątrz pętli while dodaj blok try/except, który w przypadku błędu zakończy 
wykonywanie pętli, wyświetlając komunikat o błędzie

zakończ pętlę while poleceniem, które wykona się tylko wtedy gdy pętla nie 
została w żaden sposób przerwana. Wyświetl tu komunikat o powodzeniu
'''

import os
import urllib.request

data_dir=r'E:\WszytkieProjekty\Cwiczeniea Python\PythonPozniomZaawansowany'

pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]


#for page in pages:
#    
#    try:
#        file_name=page['name']+".html"
#        path = os.path.join(data_dir,file_name)
#        
#        print("Creating file {} under process...".format(file_name))
#        urllib.request.urlretrieve(page['url'],path)
#        print("...ended with success")
#        
#    except:
#        print("File error record:",page['name'])
#        break
#else:
#    print("All the files was successfully created.")

i=0
while i<len(pages):
    
    try:
        file_name=pages[i]['name']+".html"
        path = os.path.join(data_dir,file_name)
        
        print("Creating file {} under process...".format(file_name))
        urllib.request.urlretrieve(pages[i]['url'],path)
        print("...ended with success")
        
    except:
        print("File error record:",pages[i]['name'])
        break
    i+=1

else:
    print("All the files was successfully created.")
    
#Przykład z kursuTo ten poniżej
#    
#
#pages = [
#    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
#    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
#    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]
# 
#for page in pages:
# 
#    try:
#        file_name = "{}.html".format(page["name"])
#        path = os.path.join(data_dir, file_name)
# 
#        print("Processing: {}  => {} ...".format(page["url"], file_name))
#        urllib.request.urlretrieve (page["url"], path)
#        print('...done')
#        
#    except:
#        print('FAILURE processing web page: {}'.format(page["name"]))
#        print('Stopping the process!')
#        break
# 
#else:
#    print('All pages downloaded successfully!!!')