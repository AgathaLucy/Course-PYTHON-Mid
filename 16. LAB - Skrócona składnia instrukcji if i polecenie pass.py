# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:35:12 2020

@author: 9
"""

'''
Zapisz poniższe polecenie if w postaci uproszczonej:
'''

price = 123
bonus = 23
bonus_granted = True
 
price -= bonus if bonus_granted else price
 
print(price)

'''
Zapisz poniższe polecenie if w postaci uproszczonej:
'''

rating = 5
 
print('very good') if rating == 5 else print('good') if rating == 4 else \
print('weak')

'''
Ktoś był kiedyś niezadowolony, bo w kursie jest za mało polskich akcentów, 
więc... posłuchaj piosenki De Mono - Niedziela będzie dla nas - 
https://www.youtube.com/watch?v=lmn0Qf1_eI4 (możesz też skorzystać z 
oryginalnej wersji: Niebiesko Czarnych: 
https://www.youtube.com/watch?v=Fxkhe8GqYkc)

Napisz program, który:

zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia,
bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else 
ustali co dzisiaj powinieneś robić.

Przepisz powyższy program stosując składnie uproszczona polecenia if
'''

today_weekday='piątek'

if today_weekday=='poniedziałek':
    print('Pomagam mamie')
elif today_weekday=='wtorek' or today_weekday=='sroda':
    print('Masz pranie')
elif today_weekday=='czwartek':
    print('Ja mam dyżur')
elif today_weekday=='piątek':
    print('Mam 2 zebrania')
elif today_weekday=='sobota':
    print('TY nie możesz, bo na lekcje ganiasz')
else:
    print('Niedziela jest dla nas')

#składnia uproszczona
    
print('Pomagam mamie') if today_weekday=='poniedziałek' else print('Masz pranie') \
if today_weekday=='wtorek' or today_weekday=='sroda' else print('Ja mam dyżur') \
if today_weekday=='czwartek' else print('Mam 2 zebrania') if today_weekday=='piątek' \
else print('TY nie możesz, bo na lekcje ganiasz') if today_weekday=='sobota' \
else print('Niedziela jest dla nas')