# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:21:16 2024

@author: kid30
"""

time_str=input("Nhập giờ theo định dạng giờ:phút:dây:")
gio,phut,giay=map(int,time_str.split(":"))
print("Số giây là:", gio*60*60+phut*60+giay)

