# 🏟️ SportFest: Sistem Pembelian Tiket Olahraga

## 📋 Daftar Isi
- [Flowchart](#Flowchart)
- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [Kontribusi](#kontribusi)
- [Lisensi](#lisensi)

## 💫 Flowchart



## 🌟 Pendahuluan
SportFest adalah aplikasi manajemen tiket olahraga yang memungkinkan pengguna membeli tiket untuk berbagai pertandingan olahraga dan admin mengelola jadwal pertandingan.

### Tujuan
- Mempermudah pembelian tiket pertandingan olahraga
- Memberikan kemudahan manajemen tiket untuk admin
- Menyediakan sistem pembayaran terintegrasi

## ✨ Fitur

### Fitur Pengguna
1. **Manajemen Akun**
   - Registrasi

      ```python
      def daftaruser():
       users = loadDataUser ()
       while True:
        try:
            while True:
                namaUser  = input("Masukkan nama (min 3 karakter maks 50 karakter): ").strip()
                if len(namaUser ) < 3:
                    print("Nama pengguna harus minimal 3 karakter!")
                elif len(namaUser) > 50:
                    print("Nama pengguna tidak boleh lebih dari 50 karakter!")
                elif any(user["Nama User"] == namaUser  for user in users):
                    print(f"{namaUser } sudah terdaftar.")
                else:
                    break
            
            while True:
                passwordUser  = pwinput.pwinput("Password (min 6 karakter): ", "*")
                if len(passwordUser ) < 6:
                    print("Password harus minimal 6 karakter!")
                else:
                    break

            new_user = {
                "Nama User": namaUser ,
                "Pw User": passwordUser ,
                "Saldo": 0
            }
            users.append(new_user)
            savedataUser (users)
            print('''
            +==================================================+
            |             REGISTER ANDA BERHASIL               |
            +==================================================+''')
            break
        except (ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")
      ```


   - Login User
  
     ```python
     def loginUser():
       global username
       users_data = loadDataUser()
       while True:
        try:
            if not users_data:
                print("No user data found.")
                return False
            
            print("===== LOGIN USER =====")
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ", "*")
            
            for user in users_data:
                if user["Nama User"] == username:
                    if user["Pw User"] == password:
                        print("Login berhasil!")
                        return True
                    else:
                        print("Password salah!")
                        return False
                        break
            print("Username tidak ditemukan!")
            return False
        except(ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

     ```



1. **Pembelian Tiket**
   - Pilih cabang olahraga


   ```python

   def transaksi2():
    os.system("cls")
    print("=============================================")
    print("             BELI TIKET NONTON               ")
    print("=============================================")
    if 'username' not in globals():
        print("Silakan login terlebih dahulu!")
        return
    
    while True:
        try:
            show_menu_transaksi()
            pilihan = input("Masukkan nomor tiket olahraga yang ingin anda beli (1-6): ")
            
            if pilihan == "6":
                return
            
            pilihan = int(pilihan)
            kategori_map = {
                1: 'Bola',
                2: 'Badminton',
                3: 'Basket',
                4: 'Voli',
                5: 'Futsal'
            }
            
            if pilihan in kategori_map:
                kategori_nama = kategori_map[pilihan]
                
                if pilihan == 1:
                    bola()
                elif pilihan == 2:
                    badminton()
                elif pilihan == 3:
                    basket()
                elif pilihan == 4:
                    voli()
                elif pilihan == 5:
                    futsal()
                
                pilihan_pertandingan = int(input(f"Masukkan nomor pertandingan yang ingin anda beli: "))
                
                for kategori in data['Kategori']:
                    kategori_nama = kategori["Nama Kategori"]
                    if kategori['Nama Kategori'] == kategori_nama:
                        if 0 < pilihan_pertandingan <= len(kategori['Jadwal']):
                            pertandingan = kategori['Jadwal'][pilihan_pertandingan-1]
                            
                    table = PrettyTable()
                    table.field_names = ["Detail", "Informasi"]
                    table.add_row(["Pertandingan", pertandingan['Pertandingan']])
                    table.add_row(["Kategori", pertandingan['Kategori']])
                    table.add_row(["Waktu", pertandingan['Tanggal/Waktu']])
                    table.add_row(["Harga Tiket Ekonomi", f"Rp {pertandingan['Harga Tiket Ekonomi']:,}"])
                    table.add_row(["Harga Tiket VIP", f"Rp {pertandingan['Harga Tiket VIP']:,}"])
                    
                    print(table)
                    

                    konfirmasi = input("Apakah Anda ingin membeli tiket ini? (y/n): ").lower()
                    if konfirmasi == 'y':

                        while True:
                            print("\nPilih Jenis Tiket:")
                            print("1. Tiket Ekonomi")
                            print("2. Tiket VIP")
                            jenis_tiket_choice = input("Masukkan pilihan (1/2): ")
                            
                            if jenis_tiket_choice == '1':
                                jenis_tiket = "Ekonomi"
                                harga_tiket = pertandingan['Harga Tiket Ekonomi']
                                break
                            elif jenis_tiket_choice == '2':
                                jenis_tiket = "VIP"
                                harga_tiket = pertandingan['Harga Tiket VIP']
                                break
                            else:
                                print("Pilihan tidak valid!")

                        while True:
                            try:
                                jumlah_tiket = int(input("Berapa banyak tiket yang ingin dibeli (maks 6): "))
                                if 1 <= jumlah_tiket <= 6:
                                    break
                                else:
                                    print("Jumlah tiket harus antara 1-6!")
                            except (ValueError):
                                print("Masukkan angka yang valid!")
                            except KeyboardInterrupt:
                                print("jangan tekan ctrl + C!")


                        total_harga = harga_tiket * jumlah_tiket

                        generate_invoice(username, pertandingan, jenis_tiket, jumlah_tiket, total_harga)
                        

                        while True:
                            lanjut = input("Ingin membeli tiket lagi? (y/n): ").lower()
                            if lanjut == 'y':
                                break
                            elif lanjut == 'n':
                                menu_pelanggan()
                                return
                            else:
                                print("Pilihan tidak valid!")
                    else:
                        menu_pelanggan()
                        return
                else:
                    print("Nomor pertandingan tidak valid!")
            else:
                print("Pilih angka 1-5!")
                
        except (ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

      ```
   - Beli tiket Ekonomi/VIP
   - Generate invoice

1. **Fitur Tambahan**
   - Top up saldo
   - Lihat saldo E-Money
   - Pencarian tiket
   - Sorting tiket

### Fitur Admin
1. **Manajemen Tiket**
   - Tambah tiket baru
   - Update informasi tiket
   - Hapus tiket

2. **Manajemen Jadwal**
   - Lihat jadwal pertandingan
   - Cari tiket
   - Sorting tiket

## 💻 Persyaratan Sistem
- Python 3.7+
- pip
- Library Tambahan:
  - PrettyTable
  - pwinput
  - uuid
  - datetime

## 🚀 Instalasi

### Langkah 1: Clone Repositori
```bash
git clone https://github.com/rai269/sportfest.git
cd sportfest
