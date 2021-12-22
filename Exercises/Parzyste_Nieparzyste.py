# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 22:57:44 2020

@author: 9
"""
num=int(input("Podaj liczbę: "))

if num%2==0:
    print("{} jest liczbą parzystą".format(num))
else:
    print("{} jest liczbą nieparzystą".format(num))

if num%4==0:
    print("{} jest wielokrotnocią liczby 4.".format(num))

num1=int(input("Podaj dzielnik: "))
num2=int(input("Podaj dzielną: "))

if num1%num2==0:
    print("{}/{} dzieli się bez reszty".format(num1,num2))
else:
    print("Reszta z dzielenia {}/{} to {}".format(num1,num2, num1%num2))
