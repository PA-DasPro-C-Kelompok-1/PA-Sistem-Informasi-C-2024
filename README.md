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

      ```{python}
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
  
     ```
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
   - Beli tiket Ekonomi/VIP
   - Generate invoice

2. **Fitur Tambahan**
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
