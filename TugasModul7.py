print()
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NILAI AKHIR MAHASISWA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print()
def input_data():
    n = int(input('-> Masukkan jumlah mahasiswa: '))
    data = []
    for i in range(n):
        print('\n-> Data Mahasiswa ke-', i + 1)
        nama = input('  Nama        : ')
        nim = input('  NIM         : ')
        uts = float(input('  Nilai UTS   : '))
        uas = float(input('  Nilai UAS   : '))
        tugas = float(input('  Nilai Tugas : '))
        data.append([nama, nim, uts, uas, tugas])  
    return data

def hitung_rata_rata(data, indeks):
    total = 0
    banyak = 0
    for i in range(len(data)):
        total = total + data[i][indeks]
        banyak = banyak + 1
    return total / banyak

def hitung_nilai_akhir(data):
    for i in range(len(data)):
        uts = data[i][2]
        uas = data[i][3]
        tugas = data[i][4]
        nilai = 0.35 * uas + 0.35 * uts + 0.30 * tugas
        nilai = int(nilai * 100) / 100.0
        data[i].append(nilai) 

def peringkat(data):
    n = len(data)
    for i in range(n):
        nilai_i = data[i][5]
        rank = 1
        for j in range(n):
            if data[j][5] > nilai_i:
                rank += 1
        data[i].append(rank)

def tampilkan_tabel(data):
    print('\n                                   DATA NILAI MAHASISWA')
    print('-----------------------------------------------------------------------------------------------')
    print('{:<25} {:<15} {:<8} {:<8} {:<8} {:<12} {:<9}'.format(
        '        Nama', '   NIM', 'UTS', 'UAS', 'Tugas', 'Nilai Akhir', 'Peringkat'))
    print('-----------------------------------------------------------------------------------------------')
    for i in range(len(data)):
        
        print('{:<25} {:<15} {:<8} {:<8} {:<8}    {:<12}    {:<9}'.format(
            data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6]))
        

    rata_uts = hitung_rata_rata(data, 2)
    rata_uas = hitung_rata_rata(data, 3)
    rata_tugas = hitung_rata_rata(data, 4)
    rata_akhir = hitung_rata_rata(data, 5)
    print('-----------------------------------------------------------------------------------------------')
    print('{:<25} {:<15} {:<8.2f} {:<8.2f} {:<8.2f}    {:<12.2f}'.format(
        'Rata-rata', '', rata_uts, rata_uas, rata_tugas, rata_akhir))

data_mahasiswa = input_data()
hitung_nilai_akhir(data_mahasiswa)
peringkat(data_mahasiswa)
tampilkan_tabel(data_mahasiswa)
print('\n\n#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TERIMA KASIH~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\n')