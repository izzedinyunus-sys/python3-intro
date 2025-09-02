print("--------------------------------")

#Set -> { } -> tdk berurutan, berubah, tdk duplikat
game_azka = {"valorant", "delta", "roblox"}
game_zaki = {"minecraft", "roblox"}
game_zaki.add('minecraft')
game_zaki.add('roblox')
game_azka.add('minecraft')
game_azka.add('roblox')
game_azka.remove('delta')
print("Game Azka: ", game_azka)
print("Game Zaki: ", game_zaki)
game_gabungan = game_azka | game_zaki # |> (or) atau
print("daftar game : ", game_gabungan)

#for loop utk mengeluarkan isi item dr set
for game in game_gabungan:
    print(game)
    print('---> transfer data', game, 'PS5')
#Dictionaey (Dict) -> {key:value} / {kunci:nilai}
# -> berurutan, berubah, tdk duplikat
kamus_anime = {
    "one_piece": "Monkey D Luffy",
    "blue_lock": "Isagi Ren",
    "Demon_Slayer": "Tanjiro",
    "waifu": {
        "one_piece": "big_mom",
        "demon_slayer": "nezuko",
    }
}
print("Kamus_Anime:", kamus_anime)
print("Mc_demon slayer:", kamus_anime["Demon_Slayer"])
print("Waifu one piece:", kamus_anime["waifu"]
      ["one_piece"])
#nambah item baru ke dictionary
kamus_anime["naruto"] = "Shikamaru"
print("MC naruto:", kamus_anime["naruto"])
#m3ngubah item dr dictionary
kamus_anime["demon_slayer"] = "zenitsu"
#menghapus item dr dictionary
del(kamus_anime['blue_lock'])
print("Kamus Anime Terbaru:", kamus_anime)





























