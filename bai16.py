# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:42:41 2024

@author: kid30
"""

time=input("Nhập giờ theo định dạng (vd:4h7p6s): ")
gio,phut,giay=map(int,time.replace("h"," ").replace("p"," ").replace("s"," ").split( ))
print("Số giây là:", gio*60*60+phut*60+giay)
