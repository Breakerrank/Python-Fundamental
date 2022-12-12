"""
Program perulangan dengan while sampai faham
"""
buku = 10
print('Ibu berkata: "Baca semua bukumu"')
jumlah_baca = 0

jumlah_baca_dan_faham = 0
print(f'Jumlah buku yang sudah dibaca {jumlah_baca_dan_faham}')

while jumlah_baca < buku * 2:
    jumlah_baca = jumlah_baca + 1
    if jumlah_baca_dan_faham == 7:
        print(f'Buku ke {jumlah_baca_dan_faham + 1} belum faham')
    else:
        jumlah_baca_dan_faham = jumlah_baca_dan_faham + 1
        print(f'Buku ke {jumlah_baca_dan_faham} sudah dibaca dan difahami')

print(f'Jumlah buku yang sudah dibaca dan difahami {jumlah_baca_dan_faham}')
if jumlah_baca_dan_faham == buku:
    print(f'"Bu, semua buku sudah dibaca dan difahami"')
else:
    print(f'"Bu, tidak semua buku bisa difahami. '
          f'Budi hanya bisa memahami {jumlah_baca_dan_faham} buku"')

