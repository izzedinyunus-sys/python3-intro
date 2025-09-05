buah = ["apel", "jeruk", "mangga", "durian", "cherry"]

#operasi dasar pada list

#1. mengakses elemen [index]

print(buah[2])

#2. mengubah nilainya

buah[1] = 'pisang'

print(buah)

#menambah elemen

#di akhir
buah.insert(4, 'semangka')
print(buah)

#di index terserah
buah.insert(4, 'anggur')
print(buah)

#4. menghapus elemen

#menghapus berdasarkan isi
buah.remove('cherry')
print(buah)

#menghapus berdasarkan index
buah.pop(0)
print(buah)

#5. panjang list

print(len(buah))

#6. mencetak seluruh isi list menggunakan looping

for item in buah:
    print(item)

# buat sebuah program python yang
# 1. minta user masukkin 5 nama buah, satu per satu
# 2. nama nama buah yang tadi sudah dimasukkan oleh user, simpan ke dalam list
# menggunakan append ()
# 3. tampilkan nama nama buah yang telah anda masukkan 
# contoh output:

#daftar buah anda:
# 1. mangga
# 2. semangka
# 3. pisang
# 4. anggur
# 5. durian


daftar_buah = []
for i in range(5):
    buah = input(f"Masukkan nama buah ke-{i+1}: ")
    daftar_buah.append(buah)
print("\nDaftar buah anda:")
for i in range(len(daftar_buah)):
    print(f"{i+1}. {daftar_buah[i]}")






















