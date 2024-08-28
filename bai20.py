# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:05:46 2024

@author: kid30
"""

a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c =int(input("Nhập c:"))
if b<=a and c<=a:
    print("Số lớn nhất:",a)
elif a<=b and c<=b :
    print("Số lớn nhất là:",b)
else:
    print("Số lớn nhất là:",c)
    