# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:13:46 2024

@author: kid30
"""

def cong_gio(h1,p1,s1,h2,p2,s2):
    s=s1+s2
    p=p1+p2+s//60;s%=60
    h=h1+h2+p//60;p%=60
    return h%24,p,s
def tru_gio(h1,p1,s1,h2,p2,s2):
    sa=s1-s2
    pa=p1-p1-s//60;sa %=60
    ha=h1-h2-p//60;pa %=60
    return ha%24,pa,sa
h1,p1,s1=map(int,input("Nhập giờ, phút, giây của time 1:  ").split(':'))
h2,p2,s2=map(int,input("Nhập giờ, phút, giây của time 2:  ").split(':'))
h,p,s=cong_gio(h1,p1,s1,h2,p2,s2)
ha,pa,sa=tru_gio(h1,p1,s1,h2,p2,s2)
print(f"Tổng: {h:02d}:{p:02d}:{s:02d}")
print(f"Hiệu:{ha:02d}:{pa:02d}:{sa:02d}")

                 
    