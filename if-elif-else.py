# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:47:24 2024

@author: ANVAR
"""

#bir nechta shartlarni tekshirib korishimiz kerak elif

#kun = input("Bugun nma kun? ")
#harorat = float(input('Havo qanday? '))

#if kun.lower() == 'yakshanba' and harorat > 30:
 #   print('Chomilishga ketdik')
#elif kun.lower() == 'yakshanba' and harorat < 30:
 #   print("Uydamiz!")
    
    
#boolean true false
narx = 25000
choy = 1
salat = 0
non = 1
kompot = 1
assorti = 1

#if choy:
 #   print("Mijoz choy oldi")
  #  narx = narx+3000
#if non:
 #   print("Mijoz non oldi")
  #  narx = narx+2000
#if assorti:
 #   print("Mijoz assorti oldi")
  #  narx = narx + 15000
    
#print(f"Jami {narx} sum boldi")

# in malum bir matnni royhat ichida boirmi yoqmi tekshirishimiz mumkin

menu = ['osh','manti','shashlik','lagmon']
#ovqat = input('Nima ovqat yeysiz?')
#if ovqat.lower() in menu:
 #   print('Buyurtma qabul qilindi')
#else:
 #   print('Afsuski menyuda bunday ovqat yoq!')
    
#not in bu in ni teskarisi

buyurtmalar = []
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menyuda {taom} bor")
        else:
        print(f"Kechirasiz, menyuda {taom} yoq")
else:
    print("Savatchangiz bosh")