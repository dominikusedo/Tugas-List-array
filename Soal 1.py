# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:32:52 2021

@author: Dominikus Edo Kristian - 20083000121
"""
#Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi
#Lorena di Malang
#1. set variabel kota, jarak, ongkirperkm, totongkir
#2. input pilihan kota
#3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
#jika kota Bdg, jarak = 452, ongkirperkm=4000
#4. totongkir = jarak * ongkirperkm
#5. tampilkan kota, totongkir

ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("=============================================")
    print(" TRANSKASI BIAYA EKSPEDISI ")
    print ("=============================================")
    print(" Kode = A. Surabaya")
    print(" Kode = B. Bandung")
    print ("=============================================")
    
    #jika menggunakan list Kode dibawah ini, maka metode yang digunakan
    #adalah mendeteksi indeks value yang terpilih pada list kode.
    #caranya: melakukan pencarian pada list kode menggunakan 
    # nilai kode yang diinputkan
    #salah satu metode : gunakan while
    #algoritma:
    # baca berulang2 index dalam list kode, jika value sama dengan 
    # value pilihan, ambil index nya
    
    kode =['a','b']
    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    
    pilihan = input(">> Masukkan Kode Tujuan = ")
    #identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 0
    
    #cetak tampilan layar
    print(">>> Pilihan Tujuan = " + kota[idx])
    print(">>> Jarak          = " + str(jarak[idx]) + " km")
    print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))
    
    #hitung transksi
    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm
    
    #tampilkan total ongkir
    print(">>>-------------------------------------")
    print(">>> Total Biaya     = Rp." + str(totongkir))
    ulangi = input(">> Hitung Lagi ? y/t = ")
    if ulangi== "t" or ulangi =="T":
        break