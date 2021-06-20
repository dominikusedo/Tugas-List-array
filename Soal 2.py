# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 22:35:05 2021

@author: Dominikus Edo Kristian - 20083000121
"""
merkoli = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
harga = [53000,50000,54000,45000,46000]
ppn = 0.01
diskon = 0.05

jwb = 'y'
while jwb == 'y' or jwb == 'Y' :
    print('==================================================')   
    print('                BENGKEL MOTOR UD')
    print('==================================================')
    print('1 = ',merkoli[0],'Harga = ',harga[0])
    print('2 = ',merkoli[1],'Harga = ',harga[1])
    print('3 = ',merkoli[2],'Harga = ',harga[2])
    print('4 = ',merkoli[3],'Harga = ',harga[3])
    print('5 = ',merkoli[4],'Harga = ',harga[4])
    print('==================================================')
    pilihan = int(input("Masukan Pilihan = "))   
    jumlah = int(input("Masukkan Jumlah Pembelian = "))
    idx = 0
    while idx >=0 and idx < 5 :
        idx = idx + 1
        if (pilihan - 1) == idx :
            break 
        elif pilihan == 1 :
            idx = 0
            break
    totHrgsblmppn = jumlah * harga[idx]
    totppn = totHrgsblmppn * ppn
    totHrg = totHrgsblmppn + totppn
    if totHrgsblmppn >= 200000 :
        totdiskon = totHrg * diskon
        totHrgsesudahDiskon = totHrg - totdiskon
        print('Merek Oli                  = ',merkoli[idx])
        print('Harga                      = ',harga[idx])
        print('Total Harga                = ',totHrgsblmppn)
        print('Total Harga Setelah PPN    = ',totHrg)
        print('----------------------------------------------')
        print('Total Harga Setelah Diskon = ',totHrgsesudahDiskon)
    else :
        print('Merek Oli                  = ',merkoli[idx])
        print('Harga                      = ',harga[idx])
        print('Total Harga                = ',totHrgsblmppn)  
        print('----------------------------------------------')
        print('Total Harga Setelah PPN    = ',totHrg)
    jwb = input('Beli Lagi? (y/t) : ')
    if jwb == 't' or jwb == 'T':
        break
