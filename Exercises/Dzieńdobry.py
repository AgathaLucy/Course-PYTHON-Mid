# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:14:08 2020

@author: 9
"""
import datetime as dt

def behaveYourself():
    now=dt.datetime.now().time()
    evening=dt.time(19,00,00)
    
    if now < evening:
        print("Dzień dobry")
    else:
        print("Dobry wieczór")
    
name=input("Jak masz na imię: ")
surname=input("Podaj swoje nazwisko: ")
age=int(input("Podaj swój wiek: "))
num=int(input("podaj liczbę ile razy ma być powturzona wiadomoć o urodzinach: "))
bla = dt.timedelta(days=(100-age)*365)
today = dt.datetime.today()

date = today + bla
behaveYourself()
print("{} {}, your one hudreds birhtday will be in {}.\n".format(name, surname, date )*num)