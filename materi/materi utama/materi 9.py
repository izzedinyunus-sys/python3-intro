

# function tdk akan diexekusi jika tdk dipanggil
def say_hello (name):
    # print ("Halo mr.", name)
    # kasih f di awal string utk menyisipkan variable/parameter
    # dg diapit {nama_variable}
    print(f"Halo mr. {name}")
    print("Baek baek aeee")

# lambda utk menulis fungsi yg ringkas dg 1 baris saja
# sering disebut juga fungsi anonim (tanpa nama)
say_hello_mini = lambda name: print(f"Hello mr.{name}")
# dipanggil fungsinya di bawah ini
say_hello("Azzam")
say_hello("Syahid")
print("----------------->")
say_hello_mini("Wildan")
say_hello_mini("Harun")
# cth penerapan lambda dg highder-order function
# map() -- sorted() -- filter()
jajan_mingguan = [50000, 30000, 70000, 10000, 45000, 15000]

# sorted() -> mengurutkan data
urutakn_uang = sorted(jajan_mingguan)
urutakn_uang_terbalik = sorted
print(f"Urutan Uang: {urutakn_uang}")
print(f"Urutan Uang Terbalik: {urutakn_uang_terbalik}")
# map() -> mentransformasi data
kurangin_uang = map(lambda uang: uang - 5000, jajan_mingguan)
# list() mengubah data objek map menjadi bentuk list
list_kurangin_uang = list(kurangin_uang)
print(f"Map Uang berkurang: {list_kurangin_uang}")
# filter() -> menyaring  / memfilter data
jajan_banyak = filter(lambda uang: uang >= 30000, jajan_mingguan)
list_jajan_banyak = list(jajan_banyak)
print(f"Filter jajan diatas 30rb: {list_jajan_banyak}")












