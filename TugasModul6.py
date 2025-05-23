print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~KALKULATOR MATRIKS~~~~~~~~~~~~~~~~~~~~~~')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()

barisA = int(input('Jumlah baris matriks A: '))
kolomA = int(input('Jumlah kolom matriks A: '))
print('Entri matriks A:')
A = []
for i in range(barisA):
    baris = []
    for j in range(kolomA):
        entri = float(input(f'   A[{i+1}][{j+1}]: '))
        baris.append(entri)
    A.append(baris)

barisB = int(input('\nJumlah baris matriks B: '))
kolomB = int(input('Jumlah kolom matriks B: '))
print('Entri matriks B:')
B = []
for i in range(barisB):
    baris = []
    for j in range(kolomB):
        entri = float(input(f'   B[{i+1}][{j+1}]: '))
        baris.append(entri)
    B.append(baris)

print('\nMatriks A:')
for i in range(barisA):
    print('   |', end=' ')
    for j in range(kolomA):
        print(f'{A[i][j]:.1f}', end=' ')
    print('|')

print('\nMatriks B:')
for i in range(barisB):
    print('   |', end=' ')
    for j in range(kolomB):
        print(f'{B[i][j]:.1f}', end=' ')
    print('|')

while True:
    print()
    print('\n                    MENU KALKULATOR MATRIKS\n')
    print('  1. Penjumlahan matriks')
    print('  2. Pengurangan matriks')
    print('  3. Perkalian matriks')
    print('  4. Determinan matriks (2x2)')
    print('  5. Invers matriks (2x2)')
    print('  6. Transpose matriks')
    print('  0. Keluar')

    pilihan = input('\n# Pilih operasi (0-6): ')

    if pilihan == '1':
        if barisA == barisB and kolomA == kolomB:
            hasil = []
            for i in range(barisA):
                baris = []
                for j in range(kolomA):
                    baris.append(A[i][j] + B[i][j])
                hasil.append(baris)
            print('-> Hasil Penjumlahan:')
            for baris in hasil:
                print('   |', end=' ')
                for entri in baris:
                    print(f"{entri:.1f}", end=" ")
                print('|')
        else:
            print('Ukuran matriks tidak cocok untuk penjumlahan.')

    elif pilihan == '2':
        if barisA == barisB and kolomA == kolomB:
            hasil = []
            for i in range(barisA):
                baris = []
                for j in range(kolomA):
                    baris.append(A[i][j] - B[i][j])
                hasil.append(baris)
            print('-> Hasil Pengurangan:')
            for baris in hasil:
                print('   |', end=' ')
                for entri in baris:
                    print(f'{entri:.1f}', end=' ')
                print('|')
        else:
            print('Ukuran matriks tidak cocok untuk pengurangan.')

    elif pilihan == '3':
        if kolomA == barisB:
            hasil = []
            for i in range(barisA):
                baris = []
                for j in range(kolomB):
                    total = 0
                    for k in range(kolomA):
                        total += A[i][k] * B[k][j]
                    baris.append(total)
                hasil.append(baris)
            print('-> Hasil Perkalian:')
            for baris in hasil:
                print('   |', end=' ')
                for entri in baris:
                    print(f'{entri:.1f}', end=' ')
                print('|')
        else:
            print('Ukuran matriks tidak cocok untuk perkalian.')

    elif pilihan == '4':
        print('-> Determinan Matriks A:', end=' ')
        if barisA == 2 and kolomA == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            print(detA)
        else:
            print('    Hanya mendukung determinan untuk matriks 2x2.')
        print('-> Determinan Matriks B:', end=' ')
        if barisB == 2 and kolomB == 2:
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            print(detB)
        else:
            print('    Hanya mendukung determinan untuk matriks 2x2.')

    elif pilihan == '5':
        print('-> Invers Matriks A:')
        if barisA == 2 and kolomA == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
            if detA != 0:
                invA = [
                    [ A[1][1]/detA, -A[0][1]/detA],
                    [-A[1][0]/detA,  A[0][0]/detA]
                ]
                for baris in invA:
                    print('   |', end=' ')
                    for entri in baris:
                        print(f'{entri:.1f}', end=' ')
                    print('|')
            else:
                print('    Matriks A tidak memiliki invers.')
        else:
            print('Hanya mendukung invers untuk matriks 2x2.')

        print('\n-> Invers Matriks B:')
        if barisB == 2 and kolomB == 2:
            detB = B[0][0]*B[1][1] - B[0][1]*B[1][0]
            if detB != 0:
                invB = [
                    [ B[1][1]/detB, -B[0][1]/detB],
                    [-B[1][0]/detB,  B[0][0]/detB]
                ]
                for baris in invB:
                    print('   |', end=' ')
                    for entri in baris:
                        print(f'{entri:.1f}', end=' ')
                    print('|')
            else:
                print('    Matriks B tidak memiliki invers.')
        else:
            print('Hanya mendukung invers untuk matriks 2x2.')

    elif pilihan == '6':
        print('-> Transpose Matriks A:')
        transposeA = []
        for j in range(kolomA):
            baris = []
            for i in range(barisA):
                baris.append(A[i][j])
            transposeA.append(baris)
        for baris in transposeA:
            print('   |', end=' ')
            for entri in baris:
                print(f'{entri:.1f}', end=' ')
            print('|')

        print('\n-> Transpose Matriks B:')
        transposeB = []
        for j in range(kolomB):
            baris = []
            for i in range(barisB):
                baris.append(B[i][j])
            transposeB.append(baris)
        for baris in transposeB:
            print('   |', end=' ')
            for entri in baris:
                print(f'{entri:.1f}', end=' ')
            print('|')

    elif pilihan == '0':
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('~~~~~~~TERIMA KASIH SUDAH MENGGUNAKAN KALKULATOR MATRIKS~~~~~~~~')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        break

    else:
        print(' -> PILIHAN TIDAK VALID')

        