import csv

def baca_semua(namafile='keuangan.csv'):
    with open(namafile, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # lewati header
        for row in reader:
            tanggal = row[0]
            ket = row[1]
            kategori = row[2]
            jumlah = int(row[3])
            print(f"{tanggal} | {ket} | {kategori} | Rp{jumlah}")
baca_semua()

def total_pengeluaran(namafile='keuangan.csv'):
    total = 0
    with open(namafile, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            total += int(row[3])
    return total
print("Total Pengeluaran: Rp", total_pengeluaran())

def total_per_kategori(namafile='keuangan.csv'):
    hasil = {}
    with open(namafile, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            kategori = row[2]
            jumlah = int(row[3])
            hasil[kategori] = hasil.get(kategori, 0) + jumlah
    return hasil
for kat, nilai in total_per_kategori().items():
    print(f"- {kat}: Rp{nilai}")

def kategori_terbesar(namafile='keuangan.csv'):
    per_kat = total_per_kategori(namafile)
    if not per_kat:
        return None, 0
    kat_max = max(per_kat, key=lambda k: per_kat[k])
    return kat_max, per_kat[kat_max]
kat, nilai = kategori_terbesar()
print(f"Kategori Terbesar: {kat} (Rp{nilai})")

















