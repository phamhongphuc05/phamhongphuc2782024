# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:16:20 2024

@author: kid30
"""

m=float(input("Nhập chiều dài hình chữ nhật:"))
n=float(input("Nhập chiều rộng hình chữ nhật:" ))
a=float(input("Nhập cạnh hình vuông:"))
r=float(input("Nhập bán kính hình tròn:"))
Cv=4*a
Sv=a**2
Cn=2*(n+m )
Sn=m*n 
Ct=2*r*3.14
St=3.14*r**2
print("C vuông =",Cv,"\nS vuông =",Sv,"\nC chữ nhật=",Cn,"\nS chữ nhật=",Sn,"\nC hình tròn=",Ct,"\nS hình tròn=",St)

