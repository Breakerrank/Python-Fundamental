print('Tipe data skalar => tipe data sederhana')
anak1 = 'Fachru'
anak2 = 'Abay'
anak3 = 'Cantika'
anak4 = 'Deni'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['Fachru', 'Abay', 'Cantika', 'Deni']
print(anak)
anak.append('Essy')
print(anak)

print('\nsapa anak ke-2')
print(f'hai {anak[1]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}')