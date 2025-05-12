print('\n*===================================================*')
print('*================NILAI PRAKTIKUM ADP================*')
print('*===================================================*\n')

jumlah = int(input('=> Masukkan Jumlah Mahasiswa: '))
print()

nama_mahasiswa = []
nilai_akhir = []

for i in range(jumlah):
    print(f'=> Data Mahasiswa ke-{i+1}')
    nama = input('Nama           : ')
    pretest = float(input('Nilai Pretest  : '))
    posttest = float(input('Nilai Posttest : '))
    makalah = float(input('Nilai Makalah  : '))
    print()

    hasil_akhir = 0.4 * pretest + 0.4 * posttest + 0.2 * makalah

    nama_mahasiswa.append(nama)
    nilai_akhir.append(hasil_akhir)

print('\n=> Daftar Nilai Akhir Mahasiswa <=\n')
print(f'| {"Nama Mahasiswa":<30} | {"Nilai Akhir":<14} |')
print('---------------------------------------------------')
for i in range(jumlah):
    print(f'| {nama_mahasiswa[i]:<30} | {nilai_akhir[i]:.2f}          |')

total = 0
for i in range(jumlah):
    total += nilai_akhir[i]

rata_rata = total / jumlah
print(f'\n=> Rata-rata Nilai Akhir Kelas: {rata_rata:.2f}')

tertinggi = nilai_akhir[0]
terendah = nilai_akhir[0]
nama_tertinggi = nama_mahasiswa[0]
nama_terendah = nama_mahasiswa[0]

for i in range(1, jumlah):
    if nilai_akhir[i] > tertinggi:
        tertinggi = nilai_akhir[i]
        nama_tertinggi = nama_mahasiswa[i]
    if nilai_akhir[i] < terendah:
        terendah = nilai_akhir[i]
        nama_terendah = nama_mahasiswa[i]

print(f'\n=> Nilai Tertinggi : {tertinggi:.2f} oleh {nama_tertinggi}')
print(f'=> Nilai Terendah  : {terendah:.2f} oleh {nama_terendah}')

print('\n=> Mahasiswa dengan nilai akhir di atas rata-rata :')
for i in range(jumlah):
    if nilai_akhir[i] > rata_rata:
        print(f'-> {nama_mahasiswa[i]:<20} = {nilai_akhir[i]:.2f}')


print('\n*===================================================*')
print('*===================================================*')
print('*===================================================*\n')