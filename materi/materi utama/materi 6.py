print("Materi 6 - Python Data Structure")
print("--------------------------------")

#list [berurutan, bisa diubah, boleh diduplikat]
daftar_belanja = [
    "teh desa",
    "naspad kawan lamo", 
    "pisang kembung"]
print("isi tas belanja:", daftar_belanja)
print("item ke-1", daftar_belanja[0])
print("item ke-2", daftar_belanja[1])
print("item ke-3", daftar_belanja[2])
#menambah item baru ke akhir list
daftar_belanja.append("olove chicken")
daftar_belanja.append("gabin")
print("isi tas belanja sekarang:", daftar_belanja)
print("item ke-4", daftar_belanja[3])
#remove () menghapus item dr list
daftar_belanja.remove("pisang kembung")
print("isi tas belanja akhir:", daftar_belanja)

print("-------TUPLE-------")
#tuple (berurut, tdk bisa diubah, boleh duplikat)
#penulisannya menggunakan ()
ttl = ("gresik", 16, "juni", 2009)
print("tgl lahir udin:", ttl)
#[no_index] axes data tuple
print("Tanggal:", ttl[0])
print("Bulan:", ttl[1])
print("Tahun:", ttl[2])
print("Bulan tahun:", ttl[1:2])
#akses bulan (posisi index) : lalu batas akhir item nya
print("Bulan tahun:", ttl[2:4])
#unpacking tuple ke variabel baru
#mangikuti urutan itemnya
tempat_lahir, tgl_lahir, bulan_lahir, thn_lahir = ttl
print(tempat_lahir)

#manipulasi list lanjutan
jajan_udin = ["panther", "sukro"]
jajan_koko = ["kopiko", "kopi"]
jajan_udin_dan_koko = jajan_udin + jajan_koko
print(jajan_udin_dan_koko)

#list multi-dimensi
list_minuman = [
    ["kopi", "susu", "teh"],
    ["jus apel", "jus melon", "jus jeruk"],
    ["es teler", "es campur", "es dawet"],
]
print(list_minuman)
#tiap baris punya 3 index (0, 1, 2)
print(list_minuman[2][2])
















