import json
# tambahan module 'json' dg 'import'
print("Materi 12 - JSON File Handling")
print("------- READ JSON -------")
file_path_json = r"C:\Users\Hype\Desktop\sinau IT.py\project python\materi json\materi.json"
with open(file_path_json, "r") as file_materi:
    # json.load() -> membaca isi file json
    data_materi = json.load(file_materi)
    # akses data json dg 'key' nya
    print(f"Judul berkas: {data_materi['title']}")
# akses dayta json data 'key' nya
print(f"Judul berkas: {data_materi['title']}")
print(f"Total Kelas A: {data_materi['total']}")
print(f"Status Santri: {data_materi['status_santri']}")
print(f"Status Kelulusan: {data_materi['status_santri']}")
# ekstrak data list dg for loop
for pelajaran in data_materi['pelajaran']:
    print(f"-->{pelajaran}")
# ekstrak semjua data array of object surah
# di pythion disebut juga list of dictionary
# key surah: no, nama, ayat, turun
print("-" * 50)
print("| No | Nama Surah | Ayat | Tempat Turun |")
print("-" * 50)
for surah in data_materi['surah']:
    print(f"| {surah['no']} | {surah['nama']} | {surah['ayat']} | {surah['turun']} | ")
