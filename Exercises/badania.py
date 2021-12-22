# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:49:52 2020

@author: 9
"""
#import datetime as dt
#
#print(dt.timedelta(dt.datetime.now().time())- dt.timedelta(dt.time(19,00,00)))
#
#import time
#
#print(time.strftime("%H:%M"), u">>> Wiadomość")


#tworzone listy przy pomocy modułu numpy są zagnieżdżone, aby dostać się do 
#interesujących nas elementów należy w odpowiedni sposób się do nich odwoływać


#import numpy
#
#a = [numpy.random.randint(89,size=(1, 20))]
#
#print(a)
#print(a[0])
#print(a[0][0])
#print(a[0][0][0])
#import array

#napis="Ala ma kota"
#print(napis[::-1])


#arr = [12, 34, 56, 56, 78, 78]
#print("Original Array is :",arr)
##reversing using reversed()
#result=list(reversed(arr))
#print("Resultant new reversed Array:",result)

#class MyNumbers:
#  def __iter__(self):
#    self.a = 1
#    return self
#
#  def __next__(self):
#    if self.a <= 20:
#      x = self.a
#      self.a += 1
#      return x
#    else:
#      raise StopIteration
#
#myclass = MyNumbers()
#myiter = iter(myclass)
#
#for x in myiter:
#  print(x)

#class FibIterator:
#
#    def __init__(self, n):
#        self.n = n
#        self.i = 0
#        self.a, self.b = 0, 1
#
#    def __iter__(self):
#        return self
#
#    def __next__(self):
#        if self.n == self.i:
#            raise StopIteration
#
#        self.i += 1
#        self.a, self.b = self.b, self.a + self.b
#        return self.a
#    
#print([a for a in FibIterator(10)])

#dic={9:2,0:1,3:2}
#print(dic)



#print(arr)
#print(set(arr))
#arr=list(set(arr))
##print(arr)
#arr.remove(max(arr))
##print(arr)
#print(max(arr))

#print(list(set(arr)).remove(max(arr)))
#print(max(arr))

#students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#students=[]
#
#for _ in range(int(input())):
#    name = input()
#    score = float(input())
#    students.append([name,score])
#
#
#gradesList=[]
#for l in students:
#    gradesList.append(l[1])
#
#gradesList=list(set(gradesList))
#gradesList.remove(min(gradesList))
#second=min(gradesList)
#
#for l in students:
#    if l[1]==second:
#        print(l[0])

#list=input().split(" ")
#list=[int(a) for a in list]
#print(type(list[0]))
#print(list[0][::-1])
#print(all([int(a)>0 for a in list]) and any([a==a[::-1] for a in list]))


#s='sorTiNG1234'
#print([(c, list(map(int, (c.islower(), c.isupper(), c.isdigit())))) for c in s])
#print(*sorted(s, key=lambda c: (c.isdigit(),c in '02468',c.isupper(),c.islower(),c)), sep='')
#
#dir=r'E:\WszytkieProjekty\Cwiczeniea Python\PythonPozniomZaawansowany'
#l=list(os.listdir(dir))
#print(l)
#for file in list(os.listdir(dir)):
#    print(file)


import itertools
for i in itertools.filterfalse(lambda x: x%2, range(10)):
    print(i)

print(30*"-")

for i in filter(lambda x: x%2, range(10)):
    print(i)