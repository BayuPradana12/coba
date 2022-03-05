import os
from venv import create

from numpy import delete
def layarBersih(msg):
    input(msg)
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def MainMenu(x):
    if x == "1":
        judul = input("Masukkan judul buku : ")
        create(judul)

    elif x == "2":
        readall()

    elif x == "3":
        judul = input("Masukkan judul : ")
        update()(judul)

    elif x == "4":
        judul = input("Masukkan judul buku yang ingin dihapus : ")
        delete(judul)
    
    elif x == "5":
        print("Keluar Program")
    
    else:
        print("Tidak ada Pilihan")
#1
def create(judul):
    buku.append(judul)
    layarBersih("Buku Berhasil ditambahkan")

#2
def readall():
    print("Daftar Buku :")
    no = 2
    for i in buku:
        print(str(no)+ ". "+i)
        no += 1
    layarBersih("Buku Berhasil ditambahkan")
#3
def update(judul):
filter_object = filter(lambda a: judul in a, buku)
p = list(filter_object)
if(not p):
    layarBersih("Buku Tidak ada")
else:
    layarBersih("Buku berjudul '"+",".join(p)+"' berhasil ditemukan.")
#4
def delete(judul):
    if buku.count(judul) >= 1:
        buku.remove(judul)
        layarBersih("Buku Berhasil dihapus")
    else:
        layarBersih("Buku tidak ada")
#Main
buku =["Belajar PBO, Sang Pemimpi"]

x = "0"
while x != "5":
    print("Program Buku")
    print("[1] Tambah Buku baru")
    print("[2] Lihat list buku")
    print("[3] Modifikasi Buku lama")
    print("[4] Hapus Buku lama")
    print("[5] Keluar program")
    print()

    x = input("pilihan : ")
    MainMenu(x)