#TUGAS PRAKTIKUM ADP MODUL 2

print('\n*******PEMESANAN TIKET PESAWAT*******')
nama = input('Nama Pemesan     :  ')
umur = input('Umur             :  ')
jenis_kelamin = input('Jenis Kelamin    :  ')

print('\nTujuan Yang dipilih, ')
kode = int(input('Kode Maskapai    :  '))
if kode == 3012 :
    tujuan = 'Padang-Jakarta'
    print(f'\n------------DAFTAR TIKET------------')
    print(f'Kelas Ekonomi     = Rp800000')
    print(f'Kelas Bisnis      = Rp8500000')
    print(f'Kelas First Class = Rp900000')
    jumlah = int(input('\nJumlah Tiket      : '))
    jenis = input('Jenis Maskapai    : ')
    e_3012 = 800000
    b_3012 = 850000
    fc_3012 = 900000
    if jumlah > 3 :
        if jenis == "Kelas Ekonomi"  :
            diskon = e_3012 * jumlah * 0.20 
            harga = e_3012 * jumlah - diskon
        elif  jenis == "Kelas Bisnis"  :
            diskon = b_3012 * jumlah * 0.20 
            harga = b_3012 * jumlah - diskon 
        elif jenis == "Kelas First Class"   :
            diskon = fc_3012 * jumlah * 0.20 
            harga = fc_3012 * jumlah - diskon
        else :
            print('\n~~~TIDAK ADA KELAS YANG TERSEDIA~~~\n')
            diskon = 'Tidak Tersedia' 
            harga = 'Tidak Tersedia'
        
    else :
        if jenis == "Kelas Ekonomi"   :
            diskon = 0
            harga = e_3012 * jumlah
        elif jenis == "Kelas Bisnis"  :
            diskon = 0
            harga = b_3012 * jumlah
        elif jenis == "Kelas First Class"   :
            diskon = 0
            harga = fc_3012 * jumlah
        else :
            print('\n~~~TIDAK ADA KELAS YANG TERSEDIA~~~\n')
            diskon = 'Tidak Tersedia' 
            harga = 'Tidak Tersedia'

    print(f'Total Diskon      : ',diskon)
    print(f'Total Pembayaran  : ',harga)      
    
elif kode == 4015 :
    tujuan = 'Padang-Batam'
    print(f'\n-------------DAFTAR TIKET-------------')
    print(f'Kelas Ekonomi     = Rp500000')
    print(f'Kelas Bisnis      = Rp550000')
    print(f'Kelas First Class = Rp700000')
    jumlah = int(input('\nJumlah Tiket     : '))
    jenis = input('Jenis Maskapai    : ')
    e_4015 = 500000
    b_4015 = 550000
    fc_4015 = 700000
    if jumlah > 3 :
        if jenis == "Kelas Ekonomi"  :
             diskon = e_4015 * jumlah * 0.20 
             harga = e_4015 * jumlah - diskon
        elif  jenis == "Kelas Bisnis"  :
             diskon = b_4015 * jumlah * 0.20
             harga = b_4015 * jumlah - diskon 
        elif jenis == "Kelas First Class"   :
             diskon = fc_4015 * jumlah * 0.20
             harga = fc_4015 * jumlah - diskon
        else :
            print('\n~~~TIDAK ADA KELAS YANG TERSEDIA~~~\n')
            diskon = 'Tidak Tersedia' 
            harga = 'Tidak Tersedia'
        
    else :
        if jenis == "Kelas Ekonomi"   :
            diskon = 0
            harga = e_4015 * jumlah
        elif jenis == "Kelas Bisnis"  :
            diskon = 0
            harga = b_4015 * jumlah
        elif jenis == "Kelas First Class"   :
            diskon = 0
            harga = fc_4015 * jumlah
        else :
            print('\n~~~TIDAK ADA KELAS YANG TERSEDIA~~~\n')
            diskon = 'Tidak Tersedia' 
            harga = 'Tidak Tersedia'

    print(f'Total Diskon      : {diskon :.2f}')
    print(f'Total Pembayaran  : {harga :.2f}')   
    
    

elif kode == 4050 :
    tujuan = "Padang-Bandung"
    print(f'\n-------------DAFTAR TIKET-------------')
    print(f'Kelas Ekonomi     = Rp700000')
    print(f'Kelas Bisnis      = Rp750000')
    print(f'Kelas First Class = Rp850000')

    jumlah = int(input('\nJumlah Tiket     :  '))
    jenis = input('Jenis Maskapai   : ')
    e_4050 = 700000
    b_4050 = 750000
    fc_4050 = 850000
    if jumlah > 3 :
        if jenis == "Kelas Ekonomi"  :
             diskon = e_4050 * jumlah * 0.20 
             harga = e_4050 * jumlah - diskon
        elif  jenis == "Kelas Bisnis"  :
             diskon = b_4050 * jumlah * 0.20 
             harga = b_4050 * jumlah - diskon 
        elif jenis == "Kelas First Class"   :
             diskon = fc_4050 * jumlah * 0.20 
             harga = fc_4050 * jumlah - diskon
        else :
            print('\n~~~TIDAK ADA KELAS YANG TERSEDIA~~~\n')
            diskon = 'Tidak Tersedia' 
            harga = 'Tidak Tersedia'
        
    else :
        if jenis == "Kelas Ekonomi"   :
            diskon = 0
            harga = e_4050 * jumlah
        elif jenis == "Kelas Bisnis"  :
            diskon = 0
            harga = b_4050 * jumlah
        elif jenis == "Kelas First Class"   :
            diskon = 0
            harga = fc_4050 * jumlah
        else :
            print('\n~~~TIDAK ADA KELAS YANG TERSEDIA~~~\n')
            diskon = 'Tidak Tersedia' 
            harga = 'Tidak Tersedia'
        
    print(f'Total Diskon      : {diskon :.2f}')
    print(f'Total Pembayaran  : {harga :.2f}')

    

else :
    print(f'\n----TIDAK ADA TIKET YANG TERSEDIA----\n')
    kode              = 'Tidak Valid'
    tujuan            = 'Tidak Valid'
    jenis             = 'Tidak Valid'
    jumlah            = 'Tidak Valid'
    diskon            = 'Tidak Valid'
    harga             = 'Tidak Valid'


print('\n=====================================')
print('======= STRUK PEMBELIAN TIKET =======')
print('=====================================')
print('Nama              : ',nama)
print('Umur              : ',umur)
print('Jenis Kelamin     : ',jenis_kelamin)
print('Kode Maskapai     : ',kode)
print('Tujuan            : ',tujuan)
print('Jenis Maskapai    : ',jenis)
print('Jumlah Tiket      : ',jumlah)
print(f'Total Diskon      : ',diskon)
print(f'Total Pembayaran  : ',harga)
print('=====================================')
print('=============TERIMA KASIH============')
print('=====================================\n')