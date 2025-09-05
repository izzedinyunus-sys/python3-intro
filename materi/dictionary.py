# dictionary

udin = {
    "umur": 16, 
    "asal": "gresik", 
    "kelas": "10 a"
}

# operasi pd dictionary

# 1. mengakses nilainya

print(udin["asal"])

# 2. menambahkan nilai

udin["berat_badan"] = 44
print(udin)

# 3. mengubah nilai

udin["berat_badan"] = 46
print(udin)

# 4. menghapus nilai

del(udin['berat_badan'])
print(udin)

# 5. m,engecek key

print("umur" in udin)

# 6. mendapatkan semua key dan valuenuya

# cara mengecek ada key apa aja
print(udin.keys())

# cara mengecak ada vaklue apa aja
print(udin.values())

# looping 

for key in udin:
    print(key)

for value in udin.values():
    print(value)

for key, value in udin.items():
    print(f"{key} -> {value}")

# nested dictionary

kelas = {
    "siswa1": {
        "nama": "harun", 
        "umur": 24, 
        "asal": "bogor", 
        

    }
}


















