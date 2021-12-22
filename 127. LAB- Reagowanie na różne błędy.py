# -*- coding: utf-8 -*-
"""
Created on Tue May 19 20:12:09 2020

@author: 9
"""

'''
Rozpocznij zadanie od rozwiązania z poprzedniej lekcji (jeśli nie masz swojego,
możesz skorzystać z mojego)

Obsłuż niezależnie następujące kategorie błędów:

requests.exceptions.ConnectionError - ten błąd łatwo sprowokujesz wpisując 
nieprawidłowy adres URL

PermissionError - ten błąd uzyskasz zaznaczając atrybut "tylko do odczytu" 
dla pliku spis.html

FileNotFoundError - może się pojawić w trakcie prób, gdy plik download.tmp 
nie będzie istniał, a wykonywać będzie się instrukcja kopiowania plików

Exception - ogólna obsługa błędów "na wszelki wypadek"

Obsługując błędy wyświetlaj po prostu komunikaty
'''

import requests
import os
import shutil
 
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
 
url = 'http://wwwmobilo24.eu/spis/'
dir = 'E:/WszytkieProjekty/Cwiczeniea Python/PythonPozniomZaawansowany/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)

try:
    if os.path.exists(tmpfile_path): 
        os.remove(tmpfile_path)
       
    print("Pobieranie strony: {}".format(url))
    save_url_to_file(url, tmpfile_path)
    
    print("Kopiowanie pliku '{}' do '{}'.".format(tmpfile, file))
    shutil.copyfile(tmpfile_path, file_path)

except requests.exceptions.ConnectionError as a:
    print("Wprowadzono nie poprawny adres strony {}.".format(url))
    
except PermissionError as a:    
    print("Brak uprawnień do odczytu pliku.\nSzczegóły:\n{}".format(a))

except FileNotFoundError as a:
    print("Nie odnaleziono pliku {}.\nSzczegóły:\n{}".format(tmpfile,a))

except Exception as a:
    print("Wystąpił błąd związany z linkiem: {}".format(url))
    print("Wystąpił błąd związany {}".format(tmpfile,a))

else:
    print("Operacja zakończona sukcesem!")

finally:
    if os.path.exists(tmpfile_path): 
        os.remove(tmpfile_path)
        print("Zakończono usuwanie plików tymczasowych.")
        
        