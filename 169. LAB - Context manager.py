# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:38:14 2020

@author: 9
"""
'''
Napisz context manager generujący HTML.

Nazwij go HtmlCM

W metodzie __init__ nie rób nic

W metodzie __enter__ wyświetl nagłówek tabelki HTML, mniej więcej w taki sposób:

<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>
 </TR>
W metodzie __exit__ wyświetl zamykający tag dla tabeli, mniej więcej tak:

</TABLE>

Wykorzystaj nowy context manager korzystając z odpowiedniej konstrukcji with ...

Wewnątrz context managera wyświetl 2 wiersze tabeli, mniej więcej tak:

 <TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>
'''


class HtmlCM():
    
    def __init__(self):
        pass
    
    def __enter__(self):
        print('''
<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>
 </TR>
''')
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('</TABLE>')


with HtmlCM():
    print('''
 <TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>
''')