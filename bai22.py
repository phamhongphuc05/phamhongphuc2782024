# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:31:50 2024

@author: Phạm Hồng Phúc 
"""
a=float(input("Nhập giá trị a:"))
b=float(input("Nhập giá trị b:"))
if a==0 and b==0:
    print ("phương trình vô nghiệm")
elif a==0 and b!=0:
    print ("phương trình vô số nghiệm")
else:
    print("Nghiệm của phương trình là x=",(-b/a))
    
