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



   ```python
      def proses_pembelian_tiket(pertandingan, username):
       try:
   
           if not pertandingan or not username:
               print("Error: Data tidak lengkap")
               return False
   
           print("LIMIT PEMBELIAN TIKET HANYA 5 TIKET")
           print("========================================")
           print("             1. Tiket Ekonomi           ")
           print("             2. Tiket VIP               ")
           print("========================================")
       
           while True:
               try:
                   nanyaJenis = int(input("Tiket yang ingin dibeli (1/2): "))
                   if nanyaJenis not in [1, 2]:
                       print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
                       continue
                   
                   nanya = int(input("Berapa banyak tiket yang ingin anda beli: "))
                   
   
                   if nanya > 5:
                       print("LIMIT TIKET HANYA 5 TIKET")
                       continue
                   elif nanya <= 0:
                       print("Tolong masukkan jumlah tiket yang valid!")
                       continue
   
   
                   if nanyaJenis == 1:
                       harga_tiket = pertandingan.get('Harga Tiket Ekonomi', 0)
                       jenis_tiket = "Ekonomi"
                   else:
                       harga_tiket = pertandingan.get('Harga Tiket VIP', 0)
                       jenis_tiket = "VIP"
   
                   if harga_tiket <= 0:
                       print("Error: Harga tiket tidak valid")
                       return False
   
                   total_harga = harga_tiket * nanya
   
                   users = loadDataUser()
                   for user in users:
                       if user["Nama User"] == username:
                           if user.get("Saldo", 0) >= total_harga:
                               user["Saldo"] -= total_harga
                               savedataUser(users)
                               
                               invoice_success = generate_invoice(
                                   username, 
                                   pertandingan, 
                                   jenis_tiket, 
                                   nanya, 
                                   total_harga
                               )
                               
                               if invoice_success:
                                   print(f"\nSisa saldo: Rp {user['Saldo']:,}")
                                   return True
                               else:
                                   print("Gagal membuat invoice")
                                   return False
                           else:
                               print("======================================")
                               print("\nSaldo tidak mencukupi")
                               print(f"Total harga: Rp {total_harga:,}")
                               print(f"Saldo Anda: Rp {user.get('Saldo', 0):,}")
                               print("--------------------------------------")
                               print("           1. Isi Saldo")
                               print("             2. Batal")
                               print("======================================")
                               pilihan = int(input("Masukkan pilihan: "))
                               if pilihan == 1:
                                   topUp4()
                               elif pilihan == 2:
                                   print("Pembelian tiket dibatalkan")
                                   menu_pelanggan()
                               return False
                   
                   print("User tidak ditemukan")
                   return False
               
               except (ValueError):
                   print("\n Mohon masukkan data yang valid")
               except KeyboardInterrupt:
                   print("jangan tekan ctrl + C!")
   
   
       except Exception as e:
           print(f"Terjadi kesalahan dalam proses pembelian: {e}")
           return False


      ```




   - Generate invoice
  

     ```python
        def generate_invoice(username, pertandingan, jenis_tiket, jumlah_tiket, total_harga):
          try:
              # Validasi input
              if not all([username, pertandingan, jenis_tiket, jumlah_tiket, total_harga]):
                  print("Error: Data tidak lengkap")
                  return False
   
           # Validasi tipe data
           if not isinstance(jumlah_tiket, int) or jumlah_tiket <= 0:
               print("Error: Jumlah tiket harus bilangan bulat positif")
               return False
   
           if not isinstance(total_harga, (int, float)) or total_harga <= 0:
               print("Error: Total harga harus bilangan positif")
               return False
   
           invoice_id = str(uuid.uuid4())[:8]
           current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
           invoice_content = f"""
            {'='*40}
                   STRUK PEMBELIAN TIKET SPORTFEST
            {'='*40}
            No. Invoice   : {invoice_id}
            Tanggal       : {current_time}
            Nama Pembeli  : {username}
            {'='*40}
            Pertandingan  : {pertandingan.get('Pertandingan', 'Tidak Diketahui')}
            Kategori      : {pertandingan.get('Kategori', 'Tidak Diketahui')}
            Tanggal/Waktu : {pertandingan.get('Tanggal/Waktu', 'Tidak Diketahui')}
            {'='*40}
            Jenis Tiket   : {jenis_tiket}
            Jumlah Tiket  : {jumlah_tiket}
            Harga Satuan  : Rp {pertandingan.get(f'Harga Tiket {jenis_tiket.replace(" ", "")}', 0):,}
            Total Harga   : Rp {total_harga:,}
            {'='*40}
                Terima kasih atas pembelian Anda!
            {'='*40}
            """
                    print(invoice_content)
   
           struk_path = os.path.join(os.path.dirname(__file__), 'struk.txt')
   
           with open(struk_path, 'a', encoding='utf-8') as file:
               file.write(invoice_content + "\n")
           
           print(f"\nStruk telah disimpan di {struk_path}")
           return True
       
          except Exception as e:
              print(f"Gagal membuat struk: {e}")
              import traceback
              traceback.print_exc()
              return False
         ```
      

1. **Fitur Tambahan**
   - Top up saldo



   ```python
         def topUp4():
          while True:
              os.system("cls")
              if 'username' not in globals():
                  print("Silakan login terlebih dahulu!")
                  return
                  
              print("+=================================+")
              print("|          TOP UP SALDO           |")
              print("+=================================+")
              users = loadDataUser()
              tabel = PrettyTable()
              tabel.clear_rows()
              tabel.title = "====TOP UP SALDO===="
              tabel.field_names = ["NO", "PILIHAN"]
              tabel.add_row(["[1]", "Rp 50.000"])
              tabel.add_row(["[2]", "Rp 100.000"])
              tabel.add_row(["[3]", "Rp 500.000"])
              tabel.add_row(["[4]", "Rp 1.000.000"])
              tabel.add_row(["[5]", "Rp 10.000.000"])
              tabel.add_row(["[6]", "Kembali"])
              print(tabel)
              
              try:
                  pilihan = int(input("Masukkan pilihan nominal (1-6): "))
                  
                  nominal = [50000, 100000, 500000, 1000000, 10000000]
                  
                  if 1 <= pilihan <= 5:
                      user_found = False
                      for user in users:
                          if user["Nama User"] == username:
                              user_found = True
                              konfirmasi = input(f"Anda akan top up sebesar Rp {nominal[pilihan-1]:,}. Lanjutkan? (y/n): ")
                              if konfirmasi.lower() == 'y':
                                  user["Saldo"] += nominal[pilihan - 1]
                                  savedataUser(users)
                                  print(f"Top up berhasil!")
                                  print("=====================================================")
                                  print(f"Saldo anda sekarang adalah Rp {user['Saldo']:,}")
                                  print("-----------------------------------------------------")
                                  print("                   1. Top Up lagi                    ")
                                  print("                    2. Kembali                       ")
                                  print("=====================================================")
                                  pilihan2 = int(input("Masukkan pilihan: "))
                                  if pilihan2 == 1:
                                      topUp4()
                                  elif pilihan2 == 2:
                                      menu_pelanggan()
                                  else:
                                      print("pilihan anda tidak valid atau tidak ada di menu")
                              else:
                                  print("Top up dibatalkan")
                              break
                      
                      if not user_found:
                          print("Error: User tidak ditemukan")
                          
                  elif pilihan == 6:
                      menu_pelanggan()
                  else:
                      print("Pilihan anda tidak tersedia")
                      
              except (ValueError):
                  print("\n Mohon masukkan data yang valid")
              except KeyboardInterrupt:
                  print("jangan tekan ctrl + C!")
      
              except Exception as e:
                  print(f"Terjadi kesalahan: {str(e)}")


      ```
   - Lihat saldo E-Money



   ```python
      def lihatSaldo3():
       while True:
           try:
               os.system("cls")
               if 'username' not in globals():
                   print("Silakan login terlebih dahulu!")
                   return
                   
               try:
                   users = loadDataUser()
                   user_found = False
                   
                   for user in users:
                       if user["Nama User"] == username:
                           user_found = True
                           saldo = user["Saldo"]
                           print("=========================================")
                           print(     f"SALDO ANDA ADALAH Rp {saldo:,} ")
                           print("=========================================")
   
                           print("\n==========================================")
                           print("         1. Ingin menambahkan saldo?")
                           print("                 2. Kembali")
                           print("==========================================")
   
                           pilihan = int(input("Masukkan pilihan 1/2: "))
                           if pilihan == 1:
                               topUp4()
                           elif pilihan == 2:
                               menu_pelanggan()
                           else:
                               print("Nomor pilihan tidak valid")
                           break
                           
                   if not user_found:
                       print("Error: User tidak ditemukan")
                       
               except(ValueError):
                   print("\n Mohon masukkan data yang valid")
               except KeyboardInterrupt:
                   print("jangan tekan ctrl + C!")
   
           except Exception as e:
               print(f"Terjadi kesalahan: {str(e)}")


      ```



   - Pencarian tiket
  

   ```python
      def cari5():
          os.system("cls")
          print("\n+=================================+")
          print("|            CARI TIKET           |")
          print("+=================================+")
          
       try:
           keyword = input("Masukkan kata kunci pencarian: ").lower()
           
           found = False
           table = PrettyTable()
           table.field_names = ["Kategori", "Pertandingan", "Jenis", "Waktu", "Tiket Ekonomi", "Tiket VIP"]
           
           for kategori in data['Kategori']:
               kategori_nama = kategori['Nama Kategori']
               for jadwal in kategori['Jadwal']:
                   # Mencari berdasarkan nama kategori atau nama pertandingan
                   if (keyword in kategori_nama.lower() or 
                       keyword in jadwal['Pertandingan'].lower()):
                       table.add_row([
                           kategori_nama,
                           jadwal['Pertandingan'],
                           jadwal['Kategori'],
                           jadwal['Tanggal/Waktu'],
                           f"Rp {jadwal['Harga Tiket Ekonomi']:,}",
                           f"Rp {jadwal['Harga Tiket VIP']:,}"
                       ])
                       found = True
           
           if found:
               print("\nHasil Pencarian:")
               print(table)
           else:
               print("\nTidak ditemukan hasil yang cocok dengan kata kunci pencarian.")
   
              
           pilihan = input("\ningin mencari lagi? (y/n): ")
           if pilihan == "y":
               cari5()
           elif pilihan == "n":
               menu_pelanggan()
           
       except (ValueError):
               print("\n Mohon masukkan data yang valid!")
       except KeyboardInterrupt:
               print("jangan tekan ctrl + C!")
   
       except Exception as e:
           print(f"\nTerjadi kesalahan: {str(e)}"))
   ```



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
