# Program Gaya Digital & Info Pribadi 

# 1. Info dasar dari pengguna
nama = input("Nama lengkap: ")
umur = input("Umur: ")
kelas = input("Kelas: ")
cita_cita = input("Cita-cita atau profesi impian: ")
hobi = input("Hobi favorit: ")
waktu_belajar = input("Lebih suka belajar pagi atau malam? ")

# 2. Pilih gaya digital
print("\n2. Pilih tipe gaya digital kamu (ketik angkanya aja):")
print("1. Wibu (Anak anime banget)")
print("2. Gamer (Ranked jalan terus)")
print("3. K-Popers (Ngikutin gaya Korea)")
print("4. Anak konten (Tiktoker/Youtuber wannabe)")
print("5. Anak nongki (Yang penting ngumpul)")
pilihan = input("Pilihan kamu: ")

# 3. Pertanyaan tambahan sesuai pilihan
jawaban_tambahan = ""
if pilihan == "1":
    jawaban_tambahan = input("Siapa waifu atau husbando kamu? ")
elif pilihan == "2":
    jawaban_tambahan = input("Game favorit kamu apa? ")
elif pilihan == "3":
    jawaban_tambahan = input("Siapa bias kamu? ")
elif pilihan == "4":
    jawaban_tambahan = input("Platform favorit kamu? TikTok? YouTube? ")
elif pilihan == "5":
    jawaban_tambahan = input("Nongkrong paling sering di mana? ")
else:
    print("Pilihan tidak dikenali, lanjut aja ya")

# 4. Pertanyaan bonus
bonus = input("\nPertanyaan bonus - Apakah teman di sebelah kamu bau? (ya/tidak): ")

# Menampilkan hasil lucu
print("\n--- HASIL KAMU ---")
print(f"Nama: {nama}")
print(f"Umur: {umur} tahun")
print(f"Kelas: {kelas}")
print(f"Cita-cita: {cita_cita}")
print(f"Hobi: {hobi}")
print(f"Belajar lebih suka: {waktu_belajar}")
print(f"Gaya digital kamu: ", end="")
if pilihan == "1":
    print("Wibu (Waifu/Husbando: " + jawaban_tambahan + ")")
elif pilihan == "2":
    print("Gamer (Game favorit: " + jawaban_tambahan + ")")
elif pilihan == "3":
    print("K-Popers (Bias: " + jawaban_tambahan + ")")
elif pilihan == "4":
    print("Anak Konten (Platform favorit: " + jawaban_tambahan + ")")
elif pilihan == "5":
    print("Anak Nongki (Tempat nongkrong: " + jawaban_tambahan + ")")
else:
    print("Tidak diketahui")

# Bonus lucu
if bonus.lower() == "ya":
    print("Waduh, cepet ambil parfum atau masker!")
elif bonus.lower() == "tidak":
    print("Syukurlah, temenmu aman dari bau ketek.")
else:
    print("Jawabnya ya atau tidak aja, woy!")

print("\nTerima kasih udah isi datanya!")




















