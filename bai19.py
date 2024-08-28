# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:28:44 2024

@author: kid30
"""

a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c =int(input("Nhập c:"))
d =int(input("Nhập d:"))
if a<=b and a<=c and a<=d:
    print(a)
elif b<=a and b<=c and b<= d:
    print(b)
elif c<=a and c<=b and c<=d:
    print(c)
else:
    print(d)