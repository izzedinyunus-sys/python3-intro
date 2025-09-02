# ngaji_tracker.py

def total_ngaji(halaman_list):
    return sum(halaman_list)

def cek_target(total, target=35):
    if total >= target:
        return "Tercapai 🎉"
    else:
        return "Belum tercapai 😔"
