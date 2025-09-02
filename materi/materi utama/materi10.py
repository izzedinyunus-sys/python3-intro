

# buka file
file_path = r"C:\Users\Hype\Desktop\sinau IT.py\project python.py\materi lain\pesan.txt"
# baca isi file
isi_pesan = open(file_path, "r")
# baca isi pesan
isi_pesan = isi_pesan.read()
# tampilan output isi pesan
print(f"ISI PESAN => {isi_pesan}")

print('----- OPEN CSV FILE -----')
print("                         ")


















file_path = r"C:\Users\Hype\Desktop\sinau IT.py\project python.py\materi lain\jajan.csv







isi 
print(f"TABLE JAJAN => {isi_table_jajan}")

# tutup file
file_jajan.close()

print('-------APPEND CSV FILE-------')
jajan_baru = [6,"syahid",100000]
print(f"Jajan baru: {jajan_baru}")
# open() -> membuka file dari file path
# mode 'a' -> append (tambah data)
# newline -> tambah baris baru dg teks kosong
# with ... as -> buka file dg tutup otomatis

with open(file_path_csv, "a", newline="=>") asfile_jajan:
# aktifkan mode writer csv dari file target
    writer = csv.writer(file_jajan)
# tambahkan baris dari variable jajan baru
    writer.writerow(jajan_baru)