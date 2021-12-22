# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:24:02 2020

@author: 9
"""

'''
Podążając za instrukcjami z tej lekcji wyślij sobie maila z Pythona. Jeśli nie 
masz konta na GMAIL, może się okazać, że będzie trzeba używać lekko 
zmodyfikowanych parametrów funkcji. Rozważ w takim przypadku, czy nie lepiej 
założyć sobie dodatkowe "robocze" konto GMAIL.
'''

import smtplib

mailFrom='Informacja systemowa'
mailTo=['bartholomewkokoshka@gmail.com','kokoszkabartlomiej@gmail.com']
mailSubject='Temat emaila'
mailBody='''
Hej

Ta wiadomocs zostala wgenerowana recznie, przez Tworce. Nie dopisuja na nia.

MILEGO dnia... Obserwujemy Ciebie...
'''

massage='''FROM: {}
Subject:{}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'bartholomewkokoshka@gmail.com'
password = 'kontofikcyjne1'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, massage)
    server.close()
    print('Mail was send')
except:
    print('Error durning sendding an e-mail!')
    
    
#import smtplib
# 
#mailFrom = 'Your automation system'
#mailTo = ['bartholomewkokoshka@gmail.com']
#mailSubject = 'Processing finished successfully'
#mailBody = '''Hello
# 
#This mail confirms that processing has finished without problems,
# 
#Have a nice day!'''
# 
#message = '''From: {}
#Subject: {}
# 
#{}
#'''.format(mailFrom, mailSubject, mailBody)
# 
#user = 'bartholomewkokoshka@gmail.com'
#password = 'kontofikcyjne1'
# 
#try:
#    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#    server.ehlo()
#    server.login(user,password)
#    server.sendmail(user, mailTo, message)
#    server.close()
#    print('mail sent')
#except:
#    print('error sending email')
