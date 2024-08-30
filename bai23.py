# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:48:07 2024

@author: Phạm Hồng Phúc 23706461
"""
a=float(input("Nhập giá trị a:"))
b=float(input("Nhập gía trị b:"))
c=float(input("Nhập giá trị c:"))
delta=b**2-4*a*c
if delta<0:
    print ("Phương trình vô nghiệm")
elif delta==0:
    print ("phương trình có 1 nghiệm kép","x=",(-b/2*a))
else:
    x1 = ((-b + (delta**1/2 )) / (2 * a));
    x2 = ((-b - (delta**1/2 )) / (2 * a));
    print("phương trình có 2 nghiệm phân biệt x=",x1,"x=", x2)
    

    
         
           
           
    

