
"""
Original file is located at
    https://colab.research.google.com/drive/1fRkzxQTEmkkQ4y13BbuHBhDq6VQr604l
"""

#Gate Parkir
#Membuat sebuah algoritma gate parkir untuk mendiferensiasikan tarif mobil dan motor

#Kamus
jenisKendaraan = ""       # string
idKartu = ""              # string
idKartuKeluar = ""        # string
idKartuBayar = ""         # string
metodePembayaran = ""     # string
statusPembayaran = ""     # string

waktuMasuk = 0            # integer
waktuKeluar = 0           # integer
durasiJam = 0.0           # float
jumlahJam = 0             # integer
jumlahHariInap = 0        # integer
tarifParkir = 0           # integer
saldoKartu = 0            # integer

#Algoritma
jalan = True

daftar_kartu = ["K001", "K002"]
daftar_saldo = [50000, 5000]
kartu_aktif = [False, False]
jenis_parkir = ["", ""]
waktu_masuk_parkir = [0, 0]

while jalan == True:
    print("____ SISTEM PARKIR ____ ")
    print("1. Kendaraan masuk")
    print("2. Kendaraan keluar")
    print("3. Selesai")
    menu = input("Pilih tujuan:")

    if menu == "1":
        print("Kendaraan masuk")
        jenisKendaraan = ""
        while jenisKendaraan == "":
            print("1. Mobil")
            print("2. Motor")
            print("3. Truck/Box")
            print("4. Bus")
            pilihan = input("Pilih jenis kendaraan: ")

            if pilihan == "1":
                jenisKendaraan = "Mobil"
            elif pilihan == "2":
                jenisKendaraan = "Motor"
            elif pilihan == "3":
                jenisKendaraan = "Truck/Box"
            elif pilihan == "4":
                jenisKendaraan = "Bus"
            else:
                print("Pilihan tidak valid.")

        idKartu = input("Tempelkan kartu (ID kartu): ")

        posisi = -1

        for i in range(len(daftar_kartu)):
            if daftar_kartu[i] == idKartu:
                posisi = i

        if posisi == -1:
            print("Kartu tidak dikenal.")

        elif kartu_aktif[posisi] == True:
            print("Kartu masih aktif, tidak bisa masuk.")

        else:
            waktuMasuk = float(input("Waktu masuk(0-24):"))

            if waktuMasuk < 0 or waktuMasuk > 24:
                print("Waktu tidak valid.")

            else:
                jenis_parkir[posisi] = jenisKendaraan
                waktu_masuk_parkir[posisi] = waktuMasuk
                kartu_aktif[posisi] = True
                print("Data berhasil disimpan.")
                print("Gate Parkir terbuka.")

    elif menu == "2":
        print("Kendaraan keluar.")
        idKartuKeluar = input("Tempelkan kartu (ID kartu): ")
        posisi = -1
        statusPembayaran = ""
        tarifParkir = 0

        for i in range(len(daftar_kartu)):
            if daftar_kartu[i] == idKartuKeluar:
                posisi = i

        if posisi == -1:
            print("Data parkir tidak ditemukan.")

        elif kartu_aktif[posisi] == False:
            print("Data parkir tidak ditemukan.")

        else:
            jenisKendaraan = jenis_parkir[posisi]
            waktuMasuk = waktu_masuk_parkir[posisi]
            waktuKeluar = float(input("Waktu keluar(0-24): "))

            if waktuKeluar < 0 or waktuKeluar > 24:
                print("Waktu keluar tidak valid.")

            else:
                durasiJam = waktuKeluar - waktuMasuk
                if durasiJam < 0:
                    durasiJam = durasiJam + 24
                jumlahJam = int(durasiJam)

                if durasiJam <= 24:
                    if jenisKendaraan == "Mobil":
                        tarifParkir = jumlahJam * 3000
                        if tarifParkir > 10000:
                            tarifParkir = 10000

                    elif jenisKendaraan == "Motor":
                        tarifParkir = jumlahJam * 2000
                        if tarifParkir > 5000:
                            tarifParkir = 5000

                    elif jenisKendaraan == "Truck/Box":
                        tarifParkir = jumlahJam * 3000
                        if tarifParkir > 10000:
                            tarifParkir = 10000

                    elif jenisKendaraan == "Bus":
                        tarifParkir = 20000
                else:
                    jumlahHariInap = int(durasiJam / 24)
                    if durasiJam / 24 > jumlahHariInap:
                        jumlahHariInap = jumlahHariInap + 1

                    if jenisKendaraan == "Mobil":
                        tarifParkir = jumlahHariInap * 15000

                    elif jenisKendaraan == "Motor":
                        tarifParkir = jumlahHariInap * 5000

                    elif jenisKendaraan == "Truck/Box":
                      tarifParkir = jumlahHariInap * 20000

                    elif jenisKendaraan == "Bus":
                      tarifParkir = jumlahHariInap * 20000

                print("Jenis Kendaraan:", jenisKendaraan)
                print("Durasi parkir:", durasiJam, "jam")
                print("Tarif parkir: Rp", tarifParkir)

                print("Metode Pembayaran:")
                print("1. Kartu E-money")
                print("2. QRIS")

                metodePembayaran = input("Pilih metode pembayaran:")
                if metodePembayaran == "1":
                    idKartuBayar = input("Tempelkan kartu pembayaran: ")
                    posisi_bayar = -1

                    for i in range(len(daftar_kartu)):
                        if daftar_kartu[i] == idKartuBayar:
                            posisi_bayar = i

                    if idKartuBayar != idKartuKeluar:
                        print("Kartu pembayaran tidak sesuai.")

                    elif posisi_bayar == -1:
                        print("Kartu tidak dikenal.")

                    elif daftar_saldo[posisi_bayar] >= tarifParkir:
                        daftar_saldo[posisi_bayar] -= tarifParkir
                        statusPembayaran = "Berhasil"
                        print("Pembayaran berhasil.")
                        print("Sisa saldo: Rp", daftar_saldo[posisi_bayar])

                    else:
                        print("Saldo tidak mencukupi.")
                        print("Silakan mencoba QRIS.")
                        jawab = input("Apakah pembayaran QRIS berhasil? (y/n): ")
                        if jawab == "y":
                            statusPembayaran = "Berhasil"
                            print("Pembayaran QRIS berhasil.")
                        else:
                            print("Pembayaran QRIS gagal.")

                elif metodePembayaran == "2":
                    print("Kode Qris ditampilkan.")
                    jawab = input("Apakah pembayaran QRIS berhasil? (y/n): ")
                    if jawab == "y":
                        statusPembayaran = "Berhasil"
                        print("Pembayaran QRIS berhasil.")
                    else:
                        print("Pembayaran QRIS gagal.")

                else:
                    print("Metode pembayaran tidak valid.")

                if statusPembayaran == "Berhasil":
                    kartu_aktif[posisi] = False
                    jenis_parkir[posisi] = ""
                    waktu_masuk_parkir[posisi] = 0
                    print("Data parkir berhasil dihapus.")
                    print("Kartu ditandai tidak aktif.")
                    print("Gate keluar terbuka.")
                    print("Terima kasih!")

                else:
                    print("Pembayaran belum berhasil.")
                    print("Gate tetap tertutup.")

    elif menu == "3":
        print("Sistem parkir selesai.")
        print("Terima kasih!")
        jalan = False

    else:
        print("Pilihan tidak valid.")

print("Program selesai.")

