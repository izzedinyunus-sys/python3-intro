import requests

url = f"https://api.aladhan.com/v1/timingsByCity/30-08-2025?city=Jakarta&country=Indonesia&method=20"

response = requests.get(url) # Http Get (ambil data)

data_json = response.json()

print("JADWAL SHOLAT - JSON API")

print("-" * 40)

print(data_json)
# print (data_json)
# akses data sholat berdasarkan hirarki keys yg ada
# -> data -> timings -> KeyNamaSholatNya
jadwal_sholat = data_json['data']['timings']
print(f"-> Shubuh = {jadwal_sholat['Fajr']}")
print(f"-> Dzuhur = {jadwal_sholat['Dhuhr']}")
print(f"-> Maghrib = {data_json['data']['timings']['Maghrib']}") 






