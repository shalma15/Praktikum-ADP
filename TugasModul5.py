print('\n*===================================================*')
print('*================NILAI PRAKTIKUM ADP================*')
print('*===================================================*')

jumlah = int(input('=> Masukkan Jumlah Mahasiswa: '))
print()
data = []

for i in range(jumlah):
    print('=> Data Mahasiswa ke-',i+1)
    nama = input('Nama           : ')
    pretest = float(input('Nilai Pretest  : '))
    posttest = float(input('Nilai Posttest : '))
    makalah = float(input('Nilai Makalah  : '))
    print()
    nilai_akhir = 0.4 * pretest + 0.4 * posttest + 0.2 * makalah
    data.append([nama, nilai_akhir])

print('\n=> Daftar Nilai Akhir Mahasiswa <=\n')
print(f'| {'Nama Mahasiswa':<30} | {'Nilai Akhir':<14} |')
print('---------------------------------------------------')
for i in range(jumlah):
    print(f'| {data[i][0]:<30} | {data[i][1]:.2f}          |')

total = 0
for i in range(jumlah):
    total = total + data[i][1]

rata_rata = total / jumlah
print(f'\n=> Rata-rata Nilai Akhir Kelas: {rata_rata:.2f}')

tertinggi = data[0][1]
terendah = data[0][1]
nama_tertinggi = data[0][0]
nama_terendah = data[0][0]

for i in range(1, jumlah):
    if data[i][1] > tertinggi:
        tertinggi = data[i][1]
        nama_tertinggi = data[i][0]
    if data[i][1] < terendah:
        terendah = data[i][1]
        nama_terendah = data[i][0]

print(f'\n=> Nilai Tertinggi : {tertinggi:.2f} oleh {nama_tertinggi}')
print(f'=> Nilai Terendah  : {terendah:.2f} oleh {nama_terendah}')

print('\n=> Mahasiswa dengan nilai akhir di atas rata-rata :')
for i in range(jumlah):
    if data[i][1] > rata_rata:
        print(f'-> {data[i][0]:<20} = {data[i][1]:.2f}')

print('*===================================================*')
print('*===================================================*')
print('*===================================================*\n')