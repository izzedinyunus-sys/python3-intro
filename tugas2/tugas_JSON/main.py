import json
path_file = r"C:\Users\Hype\Desktop\sinau IT.py\project python\pythopn3-intro\tugas2\tugas_JSON\peminjaman-buku.json"
with open(path_file, "r") as f:
    data = json.load(f)


total_dipinjam = 0
total_belum_kembali = 0

print("Buku yang belum kembali")
for anggota in data["anggota"]:
    for buku in anggota["pinjam"]:
        total_dipinjam += 1
        if buku['kembali'] == False:
           total_belum_kembali += 1
           print(f"- {anggota['nama']} : {buku['judul']} ({buku['tanggal']})")
           print(f"total kembali :")

print("\nRingkasan : ")
print(f"Total dipinjam: {total_dipinjam}")
print(f"Total belum kembali: {total_belum_kembali}")