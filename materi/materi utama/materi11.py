import csv
# tambahkan module 'csv'' dg 'import'
print("Materi 11 - File Handling Part 2")
print("------- UPDATE CSV -------")
# baca isi file -> ekstrak data -> buet data baru
# -> tulis ulang semua isi barisnya dg module 'w'
file_path_csv = r"C:\Users\Hype\Desktop\sinau IT.py\project python.py\materi utama\materi11.py\jajan.csv

# siapkan data jajan kosong utk menampung data dari csv ke list
data_jajan = []

# 1. baca seluruh data
with open(file_path_csv, "r") as file_jajan:

    # print(f"list data jajan => )

    #csv.reader () -> membaca isi file csv
    isi_table_jajan = file_jajan.read()

    # ekstrak semua data dg for loop
    for item_jajan in isi_table_jajan:
        print(item_jajan)












with open(file_path_csv, "r") as file_jajan:

# print(f"list data jajan => {data_jajan})

# 2. mengubah atau membuat data baru
for baris in data_jajan:
    print(f"proses item no => {item[0]}")
    print(item)
    #jika kolom nama adalah "x nama"
    if item[1] == "thufail":
        uang_jajan_baru = 15000










