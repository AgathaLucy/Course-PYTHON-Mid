# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:02:01 2020

@author: 9
"""
def hourglassSum(arr):
    list=[]
    for j in range(len(arr)-2):
        for i in range(len(arr[j])-2):
            l=sum([arr[j][i],arr[j][i+1],arr[j][i+2],arr[j+1][i+1],arr[j+2][i],arr[j+2][i+1],arr[j+2][i+2]])
            list.append(l)
    
    maxInList=max(list)
    
    return maxInList
    
arr = [[11, 12, 5, 2], [15, 6,10,4], [10, 8, 12, 5], [12,15,8,6]]

print(hourglassSum(arr))