# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:50:45 2020

@author: 9
"""


#def minimumBribes(q):
#    changes=0
#    q = [pos-1 for pos in q]
#    for pos in q:
#        if pos-q.index(pos)>2:
#            print('Too chaotic')            
#        for posC in q:
#            if posC>pos:
#                print(pos)
#    print(changes)   
    
    
    
q=[1, 2, 5, 3, 7, 8, 6, 4]

#changes=0
#for pos in q:
#    if pos-(q.index(pos)+1)>2:
#        print('Too chaotic')
#    print((q.index(pos)+1),":",pos)    
#    for posC in range(max(pos-1,0),q.index(pos)):
#        if q[posC]>pos-1:
#            changes+=1
#print(changes)

#elif pos-(q.index(pos)+1)>0 and pos-(q.index(pos)+1)<3:

def minimumBribes(q):
    changes=0
    verif=True
    for i,pos in enumerate(q):
        if pos-i>3:
            print('Too chaotic')
            verif=False
        for j,posC in enumerate(q):
            if posC > pos and j<i:
                changes+=1
    if verif:
        print(changes)
        
with open(r"E:\WszytkieProjekty\Cwiczeniea Python\PythonPozniomZaawansowany\Cwiczenia\input10.txt","r") as file:
    listOfLine=[]
    for line in file:
        if len(line)>5:
            line=line.split(" ")
            line=list(map(int,line))
            listOfLine.append(line)
            
    for p in listOfLine[1]:
        if listOfLine[1].index(p)+1!=p:
            print("{}:{}".format(listOfLine[1].index(p)+1,p))
#        print(minimumBribes(lista))
        
