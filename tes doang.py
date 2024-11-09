import json
from prettytable import PrettyTable
from operator import itemgetter
from datetime import datetime
import pwinput
import getpass
import time
import uuid
import os

PathjsonUser = r"C:\Koding\TestCode\regist.json"

# ===========
terserah = os.path.abspath(os.curdir)

json_s = "C:\\Koding\\TestCode\\schedule.json"

def load_schedule():
    with open(json_s, 'r') as data_schedule:
        return json.load(data_schedule) #load => loads,  biar sekalian diubah jadi string dan jadi format dictionary
        # return data

def save_schedule(data):
    with open(json_s, 'w') as data_schedule: 
        json.dump(data, data_schedule, indent=4)
          
data = load_schedule()
# ===========

def loadDataUser():
    try:
        with open(PathjsonUser, "r") as jsonUser:
            return json.load(jsonUser)
    except FileNotFoundError:
        return {"Nama": [], "Password": [], "saldo": []}

def savedataUser(data):
    with open(PathjsonUser, "w") as jsonUser:
        json.dump(data, jsonUser, indent=4)

#=================================================REGISTER===========================================================#

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

    
def loginAdmin():
    admin = {
        "RehanGokil": "Admin#1234",
        "SamsulBetawi": "SayaJawa",
        "MorenoPakPak": "PakPak123",
        "FakriAyamPramuka": "MintaSambelnyaMas"
    }
    username = input("Masukkan username Anda: ")
    password = pwinput.pwinput("Masukkan Password Anda: ",'*')
    if username in admin and password == admin[username]:
        return True
    else:
        return False

#==================================================================DEF-ADMINCRUD===============================================================================#
def bola():
        tabel = PrettyTable()
        tabel.title = "PERTANDINGAN BOLA"
        tabel.field_names = ["No", "Pertandingan", "Kategori", "Waktu", "Harga Tiket Ekonomi", "Harga Tiket VIP"]
        nomor = 1
        for kategori in data['Kategori']:
            if kategori['Nama Kategori'] == 'Bola':
                for match in kategori['Jadwal']:
                    tabel.add_row([f"[{nomor}]", match['Pertandingan'], match['Kategori'], match['Tanggal/Waktu'], f"Rp{match['Harga Tiket Ekonomi']:,}", f"Rp{match['Harga Tiket VIP']:,}"])
                    nomor += 1
                print(tabel)

def badminton():
        tabel = PrettyTable()
        tabel.title = "PERTANDINGAN BADMINTON"
        tabel.field_names = ["No", "Pertandingan", "Kategori", "Waktu", "Harga Tiket Ekonomi", "Harga Tiket VIP"]
        nomor = 1
        for kategori in data['Kategori']:
            if kategori['Nama Kategori'] == 'Badminton':
                for match in kategori['Jadwal']:
                    tabel.add_row([f"[{nomor}]", match['Pertandingan'], match['Kategori'], match['Tanggal/Waktu'], f"Rp{match['Harga Tiket Ekonomi']:,}", f"Rp{match['Harga Tiket VIP']:,}"])
                    nomor += 1
                print(tabel)

def basket():
        tabel = PrettyTable()
        tabel.title = "PERTANDINGAN BASKET"
        tabel.field_names = ["No", "Pertandingan", "Kategori", "Waktu", "Harga Tiket Ekonomi", "Harga Tiket VIP"]
        nomor = 1
        for kategori in data['Kategori']:
            if kategori['Nama Kategori'] == 'Basket':
                for match in kategori['Jadwal']:
                    tabel.add_row([f"[{nomor}]", match['Pertandingan'], match['Kategori'], match['Tanggal/Waktu'], f"Rp{match['Harga Tiket Ekonomi']:,}", f"Rp{match['Harga Tiket VIP']:,}"])
                    nomor += 1
                print(tabel)

def voli():
        tabel = PrettyTable()
        tabel.title = "PERTANDINGAN VOLI"
        tabel.field_names = ["No", "Pertandingan", "Kategori", "Waktu", "Harga Tiket Ekonomi", "Harga Tiket VIP"]
        nomor = 1
        for kategori in data['Kategori']:
            if kategori['Nama Kategori'] == 'Voli':
                for match in kategori['Jadwal']:
                    tabel.add_row([f"[{nomor}]", match['Pertandingan'], match['Kategori'], match['Tanggal/Waktu'], f"Rp{match['Harga Tiket Ekonomi']:,}", f"Rp{match['Harga Tiket VIP']:,}"])
                    nomor += 1
                print(tabel)
                
def futsal():
        tabel = PrettyTable()
        tabel.title = "PERTANDINGAN FUTSAL"
        tabel.field_names = ["No", "Pertandingan", "Kategori", "Waktu", "Harga Tiket Ekonomi", "Harga Tiket VIP"]
        nomor = 1
        for kategori in data['Kategori']:
            if kategori['Nama Kategori'] == 'Futsal':
                for match in kategori['Jadwal']:
                    tabel.add_row([f"[{nomor}]", match['Pertandingan'], match['Kategori'], match['Tanggal/Waktu'], f"Rp{match['Harga Tiket Ekonomi']:,}", f"Rp{match['Harga Tiket VIP']:,}"])
                    nomor += 1
                print(tabel)

def baris():
    print(" ")
    print("+=======================================================================================================================+")
    print(" ")

def khususAtmint():
    os.system("cls")
    while True:
        try:
            print("+===============================================+")
            print("|             SELAMAT DATANG ADMIN              |")
            print("+===============================================+")
            tabel = PrettyTable()
            tabel.clear_rows()
            tabel.title = "PILIHAN ADMIN"
            tabel.field_names = ["NO", "PILIHAN"]
            tabel.add_row (["[1]", "Menu Tiket"])
            tabel.add_row (["[2]", "Tambah Tiket"])
            tabel.add_row (["[3]", "Update Tiket"])
            tabel.add_row (["[4]", "Hapus Tiket"])
            tabel.add_row (["[5]", "Keluar"])
            print(tabel)
            pilihan = input("Masukkan pilihan 1/2/3/4: ")

            if pilihan == '1':
                menu()
            elif pilihan == '2':
                create()
            elif pilihan == '3':
                update()
            elif pilihan == '4':
                delete()
            elif pilihan == '5':
                main()
            else:
                print("Maaf, pilihan tidak ada di menu, masukkan pilihan yang benar")
            khususAtmint()
        except(ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")


def cari_tiket():
    while True:
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
                break

            pilihan = input("\ningin mencari lagi? (y/n): ")
            if pilihan == "y":
                cari5()
            elif pilihan == "n":
                khususAtmint()

        except KeyboardInterrupt:
            print("\nPencarian dibatalkan.")
        except Exception as e:
            print(f"\nTerjadi kesalahan: {str(e)}")

def sorting_tiket():
    os.system("cls")
    semua_pertandingan = []
    for kategori in data['Kategori']:
        for jadwal in kategori['Jadwal']:
            semua_pertandingan.append({
                'Kategori': kategori['Nama Kategori'],
                'Pertandingan': jadwal['Pertandingan'],
                'Kategori_Pertandingan': jadwal['Kategori'],
                'Tanggal/Waktu': jadwal['Tanggal/Waktu'],
                'Harga Tiket Ekonomi': jadwal['Harga Tiket Ekonomi'],
                'Harga Tiket VIP': jadwal['Harga Tiket VIP']
            })

    semua_pertandingan.sort(key=itemgetter('Pertandingan'))

    tabel = PrettyTable()
    tabel.field_names = ["Kategori", "Pertandingan", "Kategori Pertandingan", "Tanggal/Waktu", "Harga Ekonomi", "Harga VIP"]
    for pertandingan in semua_pertandingan:
        tabel.add_row([
            pertandingan['Kategori'],
            pertandingan['Pertandingan'],
            pertandingan['Kategori_Pertandingan'],
            pertandingan['Tanggal/Waktu'],
            f"Rp{pertandingan['Harga Tiket Ekonomi']:,}",
            f"Rp{pertandingan['Harga Tiket VIP']:,}"
        ])
    print(tabel)

def afterMenuAdmin():
    while True:
        try:
            tabel = PrettyTable()
            tabel.clear_rows()
            tabel.title = "SILAHKAN PILIH"
            tabel.field_names = ["NO", "PILIHAN"]
            tabel.add_row (["[1]", "Cari Tiket"])
            tabel.add_row (["[2]", "Sorting tiket (Berdasarkan abjad)"])
            tabel.add_row (["[3]", "Keluar"])
            print(tabel)
            pilihan = int(input("Masukkan pilihan 1/2/3: "))
            if pilihan == 1:
                cari_tiket()
                print("======================")
                print("   1. Cari Tiket Lain" )
                print("     2. Kembali"       )
                print("======================")
                pilihan2 = int(input("Masukkan pilihan 1/2: "))
                if pilihan2 == 1:
                    cari_tiket()
                elif pilihan2 == 2:
                    khususAtmint()
                else:
                    print("PENCARIAN ANDA TIDAK VALID, MASUKKAN PILIHAN YANG VALID")

            elif pilihan == 2:
                sorting_tiket()
                print("=====================================")
                print(  input("Tekan enter untuk kembali..."))
                print("=====================================")
                afterMenuAdmin()
                    
            elif pilihan == 3:
                khususAtmint()
                break
            else:
                print("Pilihan anda tidak ada, mohon masukkan pilihan dengan benar!!")
        except (ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

def afterMenuUser():
    while True:
        try:
            tabel = PrettyTable()
            tabel.clear_rows()
            tabel.title = "SILAHKAN PILIH"
            tabel.field_names = ["NO", "PILIHAN"]
            tabel.add_row (["[1]", "Cari Tiket"])
            tabel.add_row (["[2]", "Sorting tiket (Berdasarkan abjad)"])
            tabel.add_row (["[3]", "Keluar"])
            print(tabel)
            pilihan = int(input("Masukkan pilihan 1/2/3: "))
            if pilihan == 1:
                cari_tiket()
                print("======================")
                print("   1. Cari Tiket Lain" )
                print("     2. Kembali"       )
                print("======================")
                pilihan2 = int(input("Masukkan pilihan 1/2: "))
                if pilihan2 == 1:
                    cari_tiket()
                elif pilihan2 == 2:
                    menu_pelanggan()
                else:
                    print("PENCARIAN ANDA TIDAK VALID, MASUKKAN PILIHAN YANG VALID")

            elif pilihan == 2:
                sorting_tiket()
                print("=====================================")
                print(  input("Tekan enter untuk kembali..."))
                print("=====================================")
                afterMenuUser()
                    
            elif pilihan == 3:
                menu_pelanggan()
                break
            else:
                print("Pilihan anda tidak ada, mohon masukkan pilihan dengan benar!!")
        except (ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

def menu():
    os.system("cls")

    bola()

    baris()

    badminton()

    baris()

    basket()

    baris()

    voli()

    baris()

    futsal()

    afterMenuAdmin()

def menuUser():
    os.system("cls")

    bola()

    baris()

    badminton()

    baris()

    basket()

    baris()

    voli()

    baris()

    futsal()

    afterMenuUser()

def show_menu(is_admin=True):
    os.system("cls")
    tabel = PrettyTable()
    tabel.clear_rows()
    tabel.title = "====CABANG LOMBA===="
    tabel.field_names = ["NO", "PILIHAN"]
    tabel.add_row (["[1]", "BOLA"])
    tabel.add_row (["[2]", "BADMINTON"])
    tabel.add_row (["[3]", "BASKET"])
    tabel.add_row (["[4]", "VOLI"])
    tabel.add_row (["[5]", "FUTSAL"])
    tabel.add_row (["[6]", "KEMBALI"])
    print(tabel)
    
    pilihan = input("Masukkan pilihan (1-6): ")
    if pilihan == "6":
        if is_admin:
            khususAtmint()
        else:
            menu_pelanggan()
        return True
    return False

def show_menu_transaksi():
    tabel = PrettyTable()
    tabel.clear_rows()
    tabel.title = "====CABANG LOMBA===="
    tabel.field_names = ["NO", "PILIHAN"]
    tabel.add_row(["[1]", "BOLA"])
    tabel.add_row(["[2]", "BADMINTON"])
    tabel.add_row(["[3]", "BASKET"])
    tabel.add_row(["[4]", "VOLI"])
    tabel.add_row(["[5]", "FUTSAL"])
    tabel.add_row(["[6]", "KEMBALI"])
    print(tabel)


def create():
    os.system("cls")
    while True:
        try:
            print("=====TAMBAH TIKET======")
            tabel = PrettyTable()
            tabel.clear_rows()
            tabel.title = "MAU NAMBAH TIKET NONTON APA NIH?"
            tabel.field_names = ["NO", "PILIHAN"]
            tabel.add_row(["[1]", "BOLA"])
            tabel.add_row(["[2]", "BADMINTON"])
            tabel.add_row(["[3]", "BASKET"])
            tabel.add_row(["[4]", "VOLI"])
            tabel.add_row(["[5]", "FUTSAL"])
            tabel.add_row(["[6]", "KEMBALI"])
            print(tabel)
            pilihanCreate = int(input("Masukkan pilihan 1/2/3/4/5/6: "))

            if pilihanCreate in [1, 2, 3, 4, 5]:
                kategori_map = {1: 'Bola', 2: 'Badminton', 3: 'Basket', 4: 'Voli', 5: 'Futsal'}
                kategori_nama = kategori_map[pilihanCreate]
                
                print(f"=====TAMBAH TIKET {kategori_nama.upper()}======")

                while True:
                    pertandingan = input("Masukkan pertandingan yang ingin ditambahkan: ").strip()
                    if 3 <= len(pertandingan) <= 50:
                        break
                    else:
                        print("Nama pertandingan harus antara 3-50 karakter!")

                while True:
                    kategori = input("Masukkan kategori pertandingan: ").strip()
                    if 2 <= len(kategori) <= 20:
                        break
                    else:
                        print("Kategori harus antara 2-20 karakter!")

                while True:
                    tanggal = input("Masukkan tanggal pertandingan: ").strip()
                    if 5 <= len(tanggal) <= 20:
                        break
                    else:
                        print("Tanggal harus antara 5-20 karakter!")

                while True:
                    try:
                        hargaEkonomi = int(input("Masukkan Harga Tiket Ekonomi: "))
                        if hargaEkonomi > 0:
                            break
                        else:
                            print("Harga tiket harus lebih dari 0!")
                    except ValueError:
                        print("Masukkan angka yang valid!")

                while True:
                    try:
                        hargaVIP = int(input("Masukkan Harga Tiket VIP: "))
                        if hargaVIP > 0:
                            break
                        else:
                            print("Harga tiket harus lebih dari 0!")
                    except ValueError:
                        print("Masukkan angka yang valid!")
                
                for kategori_data in data['Kategori']:
                    if kategori_data['Nama Kategori'] == kategori_nama:
                        kategori_data['Jadwal'].append({
                            "Pertandingan": pertandingan,
                            "Kategori": kategori,
                            "Tanggal/Waktu": tanggal,
                            "Harga Tiket Ekonomi": hargaEkonomi,
                            "Harga Tiket VIP": hargaVIP
                        })
                        save_schedule(data)
                        print(f"Pertandingan {pertandingan} berhasil ditambahkan")
                        break
                else:
                    print(f"Kategori {kategori_nama} tidak ditemukan")
                
                khususAtmint()
            elif pilihanCreate == 6:
                khususAtmint()
                break
            else:
                print("Input anda tidak valid, silahkan masukkan pilihan yang tersedia!")
        except(ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

def update():
    os.system("cls")
    print("=====UPDATE TIKET=====")
    print("")
    while True:
        try:
            tabel = PrettyTable()
            tabel.clear_rows()
            tabel.title = "====CABANG LOMBA===="
            tabel.field_names = ["NO", "PILIHAN"]
            tabel.add_row(["[1]", "BOLA"])
            tabel.add_row(["[2]", "BADMINTON"])
            tabel.add_row(["[3]", "BASKET"])
            tabel.add_row(["[4]", "VOLI"])
            tabel.add_row(["[5]", "FUTSAL"])
            tabel.add_row(["[6]", "KEMBALI"])
            print(tabel)

            kategoriLomba = input("Masukkan cabang lomba (1-6): ").strip()
            
            kategori_map = {
                "1": "Bola",
                "2": "Badminton",
                "3": "Basket",
                "4": "Voli",
                "5": "Futsal"
            }
            
            # Tambahkan opsi kembali hanya di tahap awal
            if kategoriLomba == "6":
                khususAtmint()
                break
            
            if kategoriLomba in kategori_map:
                kategori_nama = kategori_map[kategoriLomba]

                tabel = PrettyTable()
                tabel.field_names = ["No", "Pertandingan", "Kategori", "Tanggal/Waktu", "Harga Ekonomi", "Harga VIP"]
                
                for kategori in data['Kategori']:
                    if kategori['Nama Kategori'] == kategori_nama:
                        for index, jadwal in enumerate(kategori['Jadwal'], 1):
                            tabel.add_row([
                                index, 
                                jadwal['Pertandingan'], 
                                jadwal['Kategori'], 
                                jadwal['Tanggal/Waktu'], 
                                f"Rp {jadwal['Harga Tiket Ekonomi']:,}", 
                                f"Rp {jadwal['Harga Tiket VIP']:,}"
                            ])
                
                print(tabel)

                nomor = int(input("Masukkan nomor yang ingin diubah: ")) - 1
                
                for kategori in data['Kategori']:
                    if kategori['Nama Kategori'] == kategori_nama:
                        if 0 <= nomor < len(kategori['Jadwal']):
                            match = kategori['Jadwal'][nomor]

                            while True:
                                pertandingan = input("Pertandingan baru: ").strip()
                                if 3 <= len(pertandingan) <= 50:
                                    break
                                else:
                                    print("Nama pertandingan harus antara 3-50 karakter!")
                            
                            while True:
                                kategori_ = input("Kategori baru: ").strip()
                                if 2 <= len(kategori_) <= 20:
                                    break
                                else:
                                    print("Kategori harus antara 2-20 karakter!")

                            while True:
                                tanggal = input("Tanggal/Waktu baru: ").strip()
                                if 5 <= len(tanggal) <= 20:
                                    break
                                else:
                                    print("Tanggal harus antara 5-20 karakter!")

                            while True:
                                try:
                                    hargaekonomi = int(input("Harga Tiket Ekonomi baru: "))
                                    if hargaekonomi > 0:
                                        break
                                    else:
                                        print("Harga tiket harus lebih dari 0!")
                                except ValueError:
                                    print("Masukkan angka yang valid!")

                            while True:
                                try:
                                    hargavip = int(input("Harga Tiket VIP baru: "))
                                    if hargavip > 0:
                                        break
                                    else:
                                        print("Harga tiket harus lebih dari 0!")
                                except ValueError:
                                    print("Masukkan angka yang valid!")
                            
                            match['Pertandingan'] = pertandingan
                            match['Kategori'] = kategori_
                            match['Tanggal/Waktu'] = tanggal
                            match['Harga Tiket Ekonomi'] = hargaekonomi
                            match['Harga Tiket VIP'] = hargavip
                            
                            save_schedule(data)
                            print(f"Data ke-{nomor+1} telah diperbarui")
                        else:
                            print("Nomor pertandingan tidak valid")
                        break
                else:
                    print("Kategori tidak ditemukan")
                
                khususAtmint()
                break
            else:
                print("Input tidak valid. Masukkan angka 1-6.")
        except(ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

def delete():
    print("=====HAPUS TIKET=====")
    print("")
    while True:
        try:
            show_menu_transaksi()
            kategoriLomba = input("Masukkan cabang lomba: ").strip()

            if kategoriLomba == "1":
                while True:
                    try:
                        bola()
                        nomor = int(input("Masukkan nomor yang mau dihapus: ")) - 1
                        for kategori in data['Kategori']:
                            if kategori['Nama Kategori'] == 'Bola':
                                if 0 <= nomor < len(kategori['Jadwal']):
                                    tiketLama = kategori['Jadwal'].pop(nomor)
                                    save_schedule(data)
                                    print(f"Paket {tiketLama['Pertandingan']} telah dihapus")
                                    input("TEKAN ENTER UNTUK MELANJUTKAN...")
                                    khususAtmint()
                                    break
                    except(ValueError):
                        print("\n Mohon masukkan data yang valid")
                    except KeyboardInterrupt:
                        print("jangan tekan ctrl + C!")


            elif kategoriLomba == "2":
                while True:
                    try:
                        badminton()
                        nomor = int(input("Masukkan nomor yang mau dihapus: ")) - 1
                        for kategori in data['Kategori']:
                            if kategori['Nama Kategori'] == 'Badminton':
                                if 0 <= nomor < len(kategori['Jadwal']):
                                    tiketLama = kategori['Jadwal'].pop(nomor)
                                    save_schedule(data)
                                    print(f"Paket {tiketLama['Pertandingan']} telah dihapus")
                                    input("TEKAN ENTER UNTUK MELANJUTKAN...")
                                    khususAtmint()
                                    break
                    except(ValueError):
                        print("\n Mohon masukkan data yang valid")
                    except KeyboardInterrupt:
                        print("jangan tekan ctrl + C!")

            elif kategoriLomba == "3":
                while True:
                    try:
                        basket()
                        nomor = int(input("Masukkan nomor yang mau dihapus: ")) - 1
                        for kategori in data['Kategori']:
                            if kategori['Nama Kategori'] == 'Basket':
                                if 0 <= nomor < len(kategori['Jadwal']):
                                    tiketLama = kategori['Jadwal'].pop(nomor)
                                    save_schedule(data)
                                    print(f"Paket {tiketLama['Pertandingan']} telah dihapus")
                                    input("TEKAN ENTER UNTUK MELANJUTKAN...")
                                    khususAtmint()
                                    break
                    except(ValueError):
                        print("\n Mohon masukkan data yang valid")
                    except KeyboardInterrupt:
                        print("jangan tekan ctrl + C!")


            elif kategoriLomba == "4":
                while True:
                    try:
                        voli()
                        nomor = int(input("Masukkan nomor yang mau dihapus: ")) - 1
                        for kategori in data['Kategori']:
                            if kategori['Nama Kategori'] == 'Voli':
                                if 0 <= nomor < len(kategori['Jadwal']):
                                    tiketLama = kategori['Jadwal'].pop(nomor)
                                    save_schedule(data)
                                    print(f"Paket {tiketLama['Pertandingan']} telah dihapus")
                                    input("TEKAN ENTER UNTUK MELANJUTKAN...")
                                    khususAtmint()
                                    break
                    except(ValueError):
                        print("\n Mohon masukkan data yang valid")
                    except KeyboardInterrupt:
                        print("jangan tekan ctrl + C!")


            elif kategoriLomba == "5":
                while True:
                    try:
                        futsal()
                        nomor = int(input("Masukkan nomor yang mau dihapus: ")) - 1
                        for kategori in data['Kategori']:
                            if kategori['Nama Kategori'] == 'Futsal':
                                if 0 <= nomor < len(kategori['Jadwal']):
                                    tiketLama = kategori['Jadwal'].pop(nomor)
                                    save_schedule(data)
                                    print(f"Paket {tiketLama['Pertandingan']} telah dihapus")
                                    input("TEKAN ENTER UNTUK MELANJUTKAN...")
                                    khususAtmint()
                    except(ValueError):
                        print("\n Mohon masukkan data yang valid")
                    except KeyboardInterrupt:
                        print("jangan tekan ctrl + C!")

                        
            else:
                print("Input anda tidak valid, silahkan masukkan cabang lomba yang tersedia!")

        except(ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

            break

#============================================================ADMIN-END=========================================================================#

def tampilkanTiket():
    os.system("cls")
    menuUser()
    afterMenuUser()

def transaksi():
    os.system("cls")
    transaksi2()

def lihatSaldo():
    os.system("cls")
    lihatSaldo3()

def topUp():
    os.system("cls")
    topUp4()

def cari():
    os.system("cls")
    cari5()


def menu_pelanggan():
    while True:
        try:  
            os.system("cls" if os.name == "nt" else "clear")
            print("+=================================================+")
            print("|           SELAMAT DATANG DI SPORTFEST           |")
            print("+-------------------------------------------------+")
            print("| TEMPAT BELI TIKET NONTON OLAHRAGA FAVORIT MU :* |")
            print("+=================================================+")
        
            print("\n")
            print("+-----------------------------------+")
            print("|           Menu Pelanggan          |")
            print("+-----------------------------------+")
            print("|     1. Tampilkan tiket            |")
            print("|     2. Beli tiket nonton          |")
            print("|     3. Lihat Saldo E-Money        |")
            print("|     4. Top Up Saldo E-Money       |")
            print("|     5. Cari                       |")
            print("|     6. Keluar                     |")
            print("+-----------------------------------+")
            
            pilih_menu = int(input("Masukkan menu yang anda inginkan (1/2/3/4/5/6): "))
            if pilih_menu == 1:
                tampilkanTiket()
            elif pilih_menu == 2:
                transaksi()
            elif pilih_menu == 3:
                lihatSaldo()
            elif pilih_menu == 4:
                topUp()
            elif pilih_menu == 5:
                cari()
            elif pilih_menu == 6:
                print("Terima kasih telah menggunakan layanan kami!")
                main()
            else: 
                print("+========================================+")
                print("| Tolong masukkan angka 1/2/3/4/5/6      |")
                print("+========================================+\n")
        except (ValueError):
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


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
        print(f"\nTerjadi kesalahan: {str(e)}")

def main():
    os.system("cls")
    while True:
        try:
            print("\n+======================= MENU ===========================+")
            print("|                 1. Register                            |")
            print("|                 2. Login user                          |")
            print("|                 3. Login admin                         |")
            print("|                 4. Keluar                              |")
            print("+========================================================+")
            pilihan = int(input("Pilih opsi (1/2/3/4): "))
            if pilihan == 1:
                daftaruser()
            elif pilihan == 2:
                if loginUser():
                    menu_pelanggan()
                else:
                    print("Username atau Password salah, silahkan coba lagi")
            elif pilihan == 3:
                    if loginAdmin() == True:
                        khususAtmint()
                        break
                    else:
                        print("Username atau Password salah, silahkan coba lagi")
            elif pilihan == 4:
                print("Program berakhir.")
                exit()
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
        except ValueError:
            print("\n Mohon masukkan data yang valid")
        except KeyboardInterrupt:
            print("jangan tekan ctrl + C!")

if __name__ == "__main__":
    main()