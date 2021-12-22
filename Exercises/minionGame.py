# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:23:53 2020

@author: 9
"""

def minion_game(string):
    string_length = len(string)
    player1, player2 = 0,0

    for i in range(string_length):
        if string[i] in "AEIOU":
            player1 += string_length - i
            print('player1',player1)
        else:
            player2 += string_length - i        
            print('player2',player2)
            
    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)