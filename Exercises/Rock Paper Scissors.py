# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 02:08:38 2020

@author: 9
"""
print("Hejka!.... Czesc, lepiej brzmi. Zagramy w papier-nozyce-kamien")

while True:
    
   
    try:
        player1=int(input("Gracz pierwszy. Wpisz numer: 1 dla papieru, 2 dla nozyczek, 3 dla kamienia: \n"))
        player2=int(input("Gracz drugi. Wpisz numer: 1 dla papieru, 2 dla nozyczek, 3 dla kamienia: \n"))
        
        if player1==player2:
            print("remis")
        elif player1==1:
            if player2==2:
                print("Wygrywa gracz drugi.")
            else:
                print("Wygrywa gracz pierwszy.")
        elif player1==2:
            if player2==3:
                print("Wygrywa gracz drugi.")
            else:
                print("Wygrywa gracz pierwszy.")
        elif player1==3:
            if player2==1:
                print("Wygrywa gracz drugi.")
            else:
                print("Wygrywa gracz pierwszy.")
        
        odp=input("Chcesz dalej grać (T/N): ")

        if odp.upper() == "N":
            break
        
    except ValueError as e:
        print('Wystąpił błąd "{}", wprowadź liczbę (1,2 lub 3) odpowiadającą figurze w grze.'.format(e))
        