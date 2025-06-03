print()
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TOKO PUSTAKA KITA~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print()

with open("inventaris_buku.txt", "w") as file:
    while True:
        print("\nMasukkan data buku (atau ketik 'selesai' di bagian ISBN untuk berhenti):")
        isbn = input("=> ISBN       : ")
        if isbn == "selesai":
            break
        judul = input("=> Judul      : ")
        penulis = input("=> Penulis    : ")
        stok = input("=> Stok       : ")
        harga_beli = input("=> Harga Beli : ")
        harga_jual = input("=> Harga Jual : ")

        baris = isbn + "," + judul + "," + penulis + "," + stok + "," + harga_beli + "," + harga_jual + "\n"
        file.write(baris)

print("\n✅ Data berhasil disimpan ke inventaris_buku.txt.")

def pecah_manual(teks):
    hasil = []
    kata = ""
    for huruf in teks:
        if huruf == ",":
            hasil.append(kata)
            kata = ""
        elif huruf == "\n":
            continue
        else:
            kata += huruf
    hasil.append(kata)
    return hasil

buku_list = []

with open("inventaris_buku.txt", "r") as file:
    for baris in file:
        bagian = pecah_manual(baris)
        buku = {
            "ISBN": bagian[0],
            "Judul": bagian[1],
            "Penulis": bagian[2],
            "Stok": int(bagian[3]),
            "Harga Beli": int(bagian[4]),
            "Harga Jual": int(bagian[5])
        }
        buku_list.append(buku)

print("📖 Data berhasil dibaca dari file.")

with open("laporan_inventaris.txt", "w") as file:
    file.write("ISBN,Judul,Penulis,Stok,Harga Beli,Harga Jual,Potensi Keuntungan\n")
    for buku in buku_list:
        keuntungan = (buku["Harga Jual"] - buku["Harga Beli"]) * buku["Stok"]
        buku["Potensi Keuntungan"] = keuntungan
        file.write(f'{buku["ISBN"]},{buku["Judul"]},{buku["Penulis"]},{buku["Stok"]},'
                   f'{buku["Harga Beli"]},{buku["Harga Jual"]},{keuntungan}\n')

print("📄 Laporan disimpan ke laporan_inventaris.txt.")

if buku_list:
    max_buku = buku_list[0]
    min_buku = buku_list[0]
    total_nilai = 0
    restock_list = []

    for buku in buku_list:
        if buku["Potensi Keuntungan"] > max_buku["Potensi Keuntungan"]:
            max_buku = buku
        if buku["Potensi Keuntungan"] < min_buku["Potensi Keuntungan"]:
            min_buku = buku
        total_nilai += buku["Stok"] * buku["Harga Beli"]
        if buku["Stok"] < 5:
            restock_list.append(buku)

    print("\n📌 Buku dengan Potensi Keuntungan Tertinggi:")
    print(f'{max_buku["Judul"]} - Rp{max_buku["Potensi Keuntungan"]}')

    print("\n📌 Buku dengan Potensi Keuntungan Terendah:")
    print(f'{min_buku["Judul"]} - Rp{min_buku["Potensi Keuntungan"]}')

    print(f"\n📦 Total Nilai Inventaris: Rp{total_nilai}")

    print("\n⚠️ Buku yang perlu di-restock (stok < 5):")
    for buku in restock_list:
        print(f'- {buku["Judul"]} (Stok: {buku["Stok"]})')
else:
    print("\n❗ Tidak ada data buku untuk dianalisis.")

print('\n#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TERIMA KASIH~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#')  
print('#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\n')