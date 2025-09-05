# main.py

import materi_tugas.doa_harian as doa_harian
import hitung_uang
import ranking
import emoji_mood
import ngaji_tracker

# -----------------------
print("=== Doa Harian ===")
doa_harian.doa_tidur()
print()
doa_harian.doa_bangun()
print()
doa_harian.doa_makan()

# -----------------------
print("\n=== Hitung Uang ===")
jajan = [50000, 30000, 15000, 70000, 10000]
print("Asli        :", jajan)
print("Bonus +5000 :", hitung_uang.tambah_bonus(jajan))
print("Yang boros  :", hitung_uang.filter_boros(jajan))

# -----------------------
print("\n=== Ranking Nilai ===")
nilai = [75, 90, 60, 88, 100, 55]
print("Nilai Desc  :", ranking.urutkan_nilai(nilai))
print("Tertinggi   :", ranking.nilai_tertinggi(nilai))
print("Terendah    :", ranking.nilai_terendah(nilai))

# -----------------------
print("\n=== Emoji Mood ===")
mood_siswa = ["senang", "biasa", "sedih", "semangat", "ga jelas"]
print("Mood Asli   :", mood_siswa)
print("Emoji Mood  :", emoji_mood.convert_mood(mood_siswa))

# -----------------------
print("\n=== Tracker Ngaji ===")
halaman = [5, 6, 4, 7, 3, 5, 8]  # contoh seminggu
total = ngaji_tracker.total_ngaji(halaman)
print("Total Halaman:", total)
print("Status Target:", ngaji_tracker.cek_target(total))
