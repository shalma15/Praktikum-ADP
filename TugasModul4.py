print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~PEMESANAN TIKET BIOSKOP~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()

while True:
    print('~MASUKKAN JUMLAH BARIS DAN KOLOM (MINIMAL 4)~')
    print()
    r = int(input('Baris : '))
    c = int(input('Kolom : '))
    if r >= 4 and c >= 4:
        break
    else:
        print()
        print('UKURAN BIOSKOP MINIMAL 4X4, SILAHKAN ULANGI.')
        print()
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()

kursi = r * c
kursi_terpesan = []

# Menampilkan layout kursi
while True:
    print('\nLAYOUT KURSI BIOSKOP:')
    print()
    nomor_kursi = 1
    for i in range(r):
        print('|', end='')
        for j in range(c):
            if str(nomor_kursi) in kursi_terpesan:
                print('  X  |', end=' ')  
            else:
                print(f'{nomor_kursi:3}  |', end=' ')  
            nomor_kursi += 1
        print()

    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print()
    print('MASUKKAN NOMOR KURSI YANG INGIN DIPESAN (0 UNTUK KELUAR)')
    print()
    pilih =input('Nomor Kursi : ')
    print()
    if pilih == '0':
        print()
        print('TERIMAKASIH TELAH MEMESAN')
        break
    
    
    if pilih in kursi_terpesan:
        print(f'KURSI {pilih} SUDAH DIPESAN, PILIH KURSI LAIN.')
    elif 1 <= int(pilih) <= kursi:
        kursi_terpesan.append(pilih) 
        print(f'KURSI NOMOR {pilih} BERHASIL DIPESAN.')
    else:
        print(f'~NOMOR KURSI {pilih} TIDAK VALID~')
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~TERIMA KASIH~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()