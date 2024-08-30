# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:39:29 2024

@author: kid30
"""

a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
c=int(input("Nhập số c:"))
if a>b and a>c:
    if b>c:
       print(f"{c} {b} {a}")
    else :
        print(f"{b} {c} {a}")
elif b>c and b>a:
    if a>c:
        print(f"{c} {a} {b}")
    else:
        print(f"{a} {c} {b}")
else:
    if a>b:
        print(f"{b} {a} {c}")
    else:
        print(f"{a} {b} {c}")
    