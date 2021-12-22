# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 23:04:38 2020

@author: 9
"""

'''
Oto klasa context managera z poprzedniego zadania:

import os
import zipfile
import requests
 
class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def __enter__(self):
        #download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
 
 
with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
 
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)
        
Dodaj do tej klasy w __exit__ obsługę błędów:

jeśli w przedostatniej linijce zmieniasz katalog na nieistniejący, to zostanie 
wygenerowany błąd: FileNotFoundError
Należy tylko wyświetlić odpowiedni komunikat o błędzie (ukryć prawdziwą przyczynę)

jeśli w ostatniej linijce użytkownik poprosi o wypakowanie nieistniejącego pliku 
to zostanie wygenerowany błąd: KeyError
Należy tylko wyświetlić odpowiedni komunikat o błędzie (ukryć prawdziwą przyczynę)

w pozostałych przypadkach błąd ma być zgłoszony na zewnątrz

Uwaga! Jeśli do błędu dochodzi w metodzie __enter__, to pokazana na tej lekcji 
metoda nie zadziała, bo wtedy blok with wcale się nie wykonuje, nie ma więc też 
metody __exit__
'''

import os
import zipfile
import requests
 
class FileFromWeb:
 
    def __init__(self, url, tmp_file):
        self.url = url
        self.tmp_file = tmp_file
 
    def __enter__(self):
        #download
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as f:
            f.write(response.content)
        return self
 
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        if exc_type==FileNotFoundError or exc_type==KeyError:
            return True
        else:
            return False
 
with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', 'c:/temp/euroxref.zip') as f:
 
    with zipfile.ZipFile(f.tmp_file, 'r') as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('c:/temp')
        z.extract(a_file, '.', None)