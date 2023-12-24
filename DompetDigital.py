class DompetDigital:
    
    def __init__(self):
        self.saldo = 1000000.0
        self.password = "123"  # Password awal

    # Menu login
    def login(self):
        input_password = input("Masukkan password: ")
        if input_password == self.password:
            print("Login berhasil!")
        else:
            print("Password salah. Silakan coba lagi.")
            exit()  # Keluar program jika login gagal

    # Menu ganti password
    def ganti_password(self):
        old_password = input("Masukkan password lama: ")
        if old_password == self.password:
            new_password = input("Masukkan password baru: ")
            self.password = new_password
            print("Password berhasil diubah!")
        else:
            print("Password lama salah. Gagal mengganti password.")

    def top_up(self, amount):
        if amount > 0:
            self.saldo += amount
            print("Top up berhasil. Saldo sekarang:", self.saldo)
        else:
            print("Jumlah top up harus lebih dari 0.")

    def cek_saldo(self):
        print("Saldo Anda saat ini:", self.saldo)
        
    def tarik_uang(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= amount
            print("Penarikan berhasil. Saldo sekarang:", self.saldo)
        elif amount <= 0:
            print("Jumlah penarikan harus lebih dari 0.")
        else:
            print("Saldo tidak mencukupi untuk penarikan tersebut.")

    def transfer(self, target, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= amount
            target.top_up(amount)
            print("Transfer berhasil. Saldo sekarang:", self.saldo)
        elif amount <= 0:
            print("Jumlah transfer harus lebih dari 0.")
        else:
            print("Saldo tidak mencukupi untuk transfer tersebut.")


if __name__ == "__main__":
    dompet = DompetDigital()

    # Login sebelum masuk ke menu utama
    dompet.login()

    while True:
        print("\nMenu:")
        print("1. Top Up")
        print("2. Cek Saldo")
        print("3. Tarik Uang")
        print("4. Transfer")
        print("5. Pengaturan (Ganti Password)")
        print("0. Keluar")

        menu = input("Pilih menu (0-5): ")

        if menu == '1':
            top_up_amount = float(input("Masukkan jumlah top up: "))
            dompet.top_up(top_up_amount)
        elif menu == '2':
            dompet.cek_saldo()
        elif menu == '3':
            tarik_amount = float(input("Masukkan jumlah penarikan: "))
            dompet.tarik_uang(tarik_amount)
        elif menu == '4':
            target_dompet = DompetDigital()  # Simulasi dompet tujuan
            transfer_amount = float(input("Masukkan jumlah transfer: "))
            dompet.transfer(target_dompet, transfer_amount)
        elif menu == '5':
            # Menu pengaturan
            dompet.ganti_password()
        elif menu == '0':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
