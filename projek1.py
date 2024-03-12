from datetime import datetime

data_hotel = []

def hitung_harga(kelas_hotel, jumlah_hari, jumlah_orang):
    # Penentuan harga berdasarkan kelas hotel
    per_malam = 0
    if kelas_hotel == "Kelas Standar":
        per_malam = 300000
    elif kelas_hotel == "Kelas Bisnis":
        per_malam = 450000
    elif kelas_hotel == "Kelas Premium":
        per_malam = 600000
    elif kelas_hotel == "Kelas VIP":
        per_malam = 1000000
    else:
        print("Kelas yang anda masukan tidak valid.")
        return

    total_harga = per_malam * jumlah_hari * jumlah_orang
    return total_harga

def insert_data():
    print("Masukkan Data")
    nama = input("Masukkan nama tamu: ")
    nomor_kamar = input("Masukkan nomor kamar: ")
    cek_in = input("Masukkan tanggal check-in (format: DD-MM-YYYY): ")
    cek_out = input("Masukkan tanggal check-out (format: DD-MM-YYYY): ")

    tanggal_check_in = datetime.strptime(cek_in, "%d-%m-%Y")
    tanggal_check_out = datetime.strptime(cek_out, "%d-%m-%Y")

    if tanggal_check_out <= tanggal_check_in:
        print("Tanggal check-out harus setelah tanggal check-in. Silakan masukkan kembali.")
        return

    jumlah_hari = (tanggal_check_out - tanggal_check_in).days

    print("\n========== PILIH KELAS ANDA ==========")
    print("1. Kelas Standar - Rp300.000")
    print("2. Kelas Bisnis - Rp450.000")
    print("3. Kelas Premium - Rp600.000")
    print("4. Kelas VIP - Rp1.000.000")

    klas = int(input("Masukkan kelas yang anda inginkan (1-4): "))

    if klas == 1:
        kelas_hotel = "Kelas Standar"
    elif klas == 2:
        kelas_hotel = "Kelas Bisnis"
    elif klas == 3:
        kelas_hotel = "Kelas Premium"
    elif klas == 4:
        kelas_hotel = "Kelas VIP"
    else:
        print("Kelas yang anda masukan tidak valid.")
        return

    # Choose the number of people staying
    print("\n========== PILIH JUMLAH ORANG ==========")
    print("1. 1 Orang")
    print("2. 2 Orang")
    print("3. 4 Orang")
    print("4. 6 Orang")

    yang_nginap = int(input("Masukkan jumlah orang yang menginap (1-4): "))
    
    if yang_nginap == 1:
        jumlah_orang = 1
    elif yang_nginap == 2:
        jumlah_orang = 2
    elif yang_nginap == 3:
        jumlah_orang = 4
    elif yang_nginap == 4:
        jumlah_orang = 6
    else:
        print("Jumlah orang yang anda masukkan tidak valid.")
        return

    # Menghitung total harga
    total_harga = hitung_harga(kelas_hotel, jumlah_hari, jumlah_orang)

    info_tamu = {
        "Nama": nama,
        "Nomor Kamar": nomor_kamar,
        "Tanggal Check-in": tanggal_check_in.strftime("%d-%m-%Y"),
        "Tanggal Check-out": tanggal_check_out.strftime("%d-%m-%Y"),
        "Jumlah Hari": jumlah_hari,
        "Kelas Hotel": kelas_hotel,
        "Jumlah Orang": jumlah_orang,
        "Harga Per Malam": hitung_harga(kelas_hotel, 1, jumlah_orang),  # Harga per malam untuk informasi tamu
        "Total Harga": total_harga
    }

    data_hotel.append(info_tamu)
    print(f"Data berhasil dimasukkan!\nTotal Harga: Rp.{total_harga:,}\n")

# ... (rest of the code remains unchanged)


def delete_data():
    print("Hapus Data")
    nama_hapus = input("Masukkan nama tamu yang akan dihapus: ")

    for tamu in data_hotel:
        if tamu["Nama"] == nama_hapus:
            data_hotel.remove(tamu)
            print("Data berhasil dihapus!\n")
            return

    print("Tamu tidak ditemukan!\n")

def display_data():
    print("Tampilkan Data")
    if not data_hotel:
        print("Tidak ada data yang tersedia.")
    else:
        for index, tamu in enumerate(data_hotel, start=1):
            print(f"\nTamu {index}:")
            for key, value in tamu.items():
                if key == "Makanan" and value is not None:
                    print(f"{key}: {value} - Rp.{hitung_harga(tamu['Kelas Hotel'], tamu['Jumlah Hari'], value):,}")
                else:
                    print(f"{key}: {value}")
        print()

def pencarian(kunci, nilai):
    rendah, tinggi = 0, len(data_hotel) - 1

    while rendah <= tinggi:
        tengah = (rendah + tinggi) // 2
        if data_hotel[tengah][kunci] == nilai:
            return tengah
        elif data_hotel[tengah][kunci] < nilai:
            rendah = tengah + 1
        else:
            tinggi = tengah - 1
    return -1

def sorting_data(kunci):
    print("Pengurutan Data")
    data_hotel.sort(key=lambda x: x[kunci])
    print("Data berhasil diurutkan!\n")

def searching_data(kunci):
    print("Pencarian Data")
    nilai_pencarian = input(f"Masukkan {kunci.lower()} untuk dicari: ")
    indeks = pencarian(kunci, nilai_pencarian)

    if indeks != -1:
        print("\nTamu ditemukan:")
        for key, value in data_hotel[indeks].items():
            print(f"{key}: {value}")
        print()
    else:
        print("Tamu tidak ditemukan!\n")

if __name__ == "__main__":
    while True:
        print("=" * 30)
        print("\tHOTEL MANADO")
        print("=" * 30)
        print("1. Insert Data")
        print("2. Delete Data")
        print("3. Display Data")
        print("4. Sorting Data")
        print("5. Searching Data")
        print("6. EXIT!!")

        pilihan = input("Masukkan pilihan Anda (1-6): ")

        if pilihan == "1":
            insert_data()
        elif pilihan == "2":
            delete_data()
        elif pilihan == "3":
            display_data()
        elif pilihan == "4":
            kunci_urut = input("Masukkan kunci untuk diurutkan (contoh, 'Nama', 'Nomor Kamar'): ")
            sorting_data(kunci_urut)
        elif pilihan == "5":
            kunci_pencarian = input("Masukkan kunci untuk dicari (contoh, 'Nama', 'Nomor Kamar'): ")
            searching_data(kunci_pencarian)
        elif pilihan == "6":
            print("Keluar dari program. Selamat tinggal!")
            break
        else:
            print("Pilihan tidak valid. Harap masukkan angka dari 1 hingga 6.\n")
