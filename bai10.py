# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:38:25 2024

@author: kid30
"""

a=int(input("Nhập số thứ nhất: "))
b=int(input("Nhập số thứ hai: "))
c=int(input("Nhập số thứ ba: "))
d=int(input("Nhập số thứ bốn: "))
t=a+b+c+d
print(f"Biển số xe là:{a}{b}{c}{d}")
N=t//10
n=t%10
sonut=N+n 
if sonut<= 10 :
   print("số nút là:",sonut)
else:
    N1=sonut//10
    n1 =sonut%10
    sonut2 =N1 +n1 
    print("Số nút là:",sonut2 )
    
    
    
