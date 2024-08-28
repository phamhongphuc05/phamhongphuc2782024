# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:34:34 2024

@author: kid30
"""

N=int(input("Nhập số tự nhiên có 2 chữ số:"))
if 10<=N<=100 :
    a=N//10 
    b=N%10 
    Tổng= a+b 
    print(f"Tổng của 2 chữ số là {Tổng}")
    