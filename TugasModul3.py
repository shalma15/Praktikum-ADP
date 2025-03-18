print('\n*===================================================*')
print('*==================TEBAK ANGKA BOM==================*')
print('*===================================================*')

print('\n~Pemain Pertama Menentukan Batas Angka Positif~\n')
nama_1 = input('Pemain 1 : ')
n = int(input('Batas Angka Yang Dipilih : '))
k = int(input('Angka BOM: '))
print('\n')
for i in range(1, n + 1):
    if i % k == 0: 
        print('BOM', end=' ')
    else:
        print(i, end=' ')
print('\n')

print('*===================================================*')
print('\n~Pemain Kedua Menebak Angka Dari 1 Hingga Yang Ditentukan Oleh Pemain 1~\n')

while True:
    nama_2 = input('Pemain 2 : ')
    s = int(input('Angka Yang Dipilih : '))
    if 1 <= s <= n: 
        if s % k == 0:
            print('\nSayang Sekali',nama_2, 'Angka', s, 'adalah BOM, Kamu kalah -_-\n')
        else:
            print('\nSelamat',nama_2, 'Angka', s, 'bukan BOM, Kamu menang ^.^\n')
        break
    else:
        print('Tebakan Kamu diluar rentang 1 -', n, 'coba lagi.\n')

print('*===================================================*')
print('*=====================GAME OVER=====================*')
print('*===================================================*\n') 