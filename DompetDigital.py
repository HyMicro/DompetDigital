import tkinter as tk
from tkinter import simpledialog, messagebox

class DompetDigital:
    def __init__(self):
        self.saldo = 1000000.0
        self.username = "admin"
        self.password = "123"  # Password awal
        self.informasi_pengguna = "Belum ada informasi pengguna."
        self.daftar_penerima = ["Ahyad", "Adytia", "Kemal"]

    def validate_login(self, username, password):
        return username == self.username and password == self.password

    def top_up(self, amount):
        if amount > 0:
            self.saldo += amount
            formatted_saldo = "{:,.2f}".format(self.saldo)
            print("Top up berhasil. Saldo sekarang: Rp. ", formatted_saldo)
        else:
            print("Jumlah top up harus lebih dari Rp. 0.")

    def cek_saldo(self):
        return f"Saldo Anda saat ini: Rp. {self.saldo:,.2f}"

    def tarik_uang_gui(self, amount):
        if 0 < amount <= self.saldo:
            self.saldo -= amount
            formatted_saldo = "{:,.2f}".format(self.saldo)
            result_message = f"Penarikan berhasil. Saldo sekarang: Rp. {formatted_saldo}"
            print(result_message)  # Print the information to the terminal
            return result_message
        elif amount <= 0:
            return "Jumlah penarikan harus lebih dari Rp. 0."
        else:
            return "Saldo tidak mencukupi untuk penarikan tersebut."

    def informasi_pengguna_menu(self):
        return f"Informasi Pengguna:\n{self.informasi_pengguna}"

    def tentang_menu(self):
        return ("Dompet Digital v1.0.3\n"
                "Dikembangkan oleh Kelompok 7 Pemrograman Lanjut H\n"
                "Teknik Informatika, Universitas Muhammadiyah Malang, Tahun 2023\n"
                "Oleh :\n"
                "Ahyad Izzuddin Syuhaiba (202210370311137)\n"
                "Adytia Bagus Saputra (202210370311144)\n"
                "Kemaldin Ahmada Syah (202210370311160)")

    def tampilkan_informasi_pengguna(self):
        return f"Informasi Pengguna:\nNama Pengguna: {self.username}\nInformasi Tambahan: {self.informasi_pengguna}"

    def ubah_informasi_pengguna(self, new_info):
        self.informasi_pengguna = new_info
        return "Informasi pengguna berhasil diubah!"

    def get_daftar_penerima_menu(self):
        return f"Daftar Penerima: {', '.join(self.daftar_penerima)}"
    
    def transfer(self, target_username, amount):
        if amount > 0:
            if target_username in self.daftar_penerima:
                self.saldo -= amount
                formatted_saldo = "{:,.2f}".format(self.saldo)
                return f"Transfer berhasil. Saldo sesudah transfer: Rp. {formatted_saldo}"
            else:
                return "Penerima dengan nama pengguna tersebut tidak ditemukan."
        elif amount <= 0:
            return "Jumlah transfer harus lebih dari Rp. 0."
        else:
            return "Saldo tidak mencukupi untuk transfer tersebut."
        
class DompetDigitalGUI(tk.Tk):
    def __init__(self, dompet):
        super().__init__()
        self.title("Dompet Digital GUI")
        self.dompet = dompet
        self.create_login_screen()

    def create_login_screen(self):
        login_frame = tk.Frame(self)
        login_frame.pack(pady=50)

        tk.Label(login_frame, text="Username:").grid(row=0, column=0, padx=5)
        self.username_entry = tk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=5)

        tk.Label(login_frame, text="Password:").grid(row=1, column=0, padx=5)
        self.password_entry = tk.Entry(login_frame, show="*")  # Hide the password
        self.password_entry.grid(row=1, column=1, padx=5)

        tk.Button(login_frame, text="Login", command=self.validate_login).grid(row=2, column=0, columnspan=2, pady=10)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.dompet.validate_login(username, password):
            messagebox.showinfo("Login successful", "Login Successful!")
            self.login_success()
        else:
            messagebox.showerror("Login Gagal", "Nama pengguna atau password salah. Silakan coba lagi.")

    def login_success(self):
        # Hapus frame login
        self.destroy_login_frame()

        # Tampilkan main frame
        self.create_main_widgets()

    def destroy_login_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_main_widgets(self):
        main_frame = tk.Frame(self)
        main_frame.pack(pady=30)

        tk.Button(main_frame, text="Cek Saldo", command=self.cek_saldo).grid(row=0, column=0, padx=5, )
        tk.Button(main_frame, text="Top Up", command=self.top_up).grid(row=1, column=0, padx=5)
        tk.Button(main_frame, text="Tarik Uang", command=self.tarik_uang_gui).grid(row=2, column=0, padx=5)
        tk.Button(main_frame, text="Daftar Penerima", command=self.tampilkan_daftar_penerima).grid(row=3, column=0, padx=5)
        tk.Button(main_frame, text="Transfer", command=self.transfer_gui).grid(row=4, column=0, padx=5)
        tk.Button(main_frame, text="Pengaturan", command=self.pengaturan_menu).grid(row=5, column=0, padx=5)
        tk.Button(main_frame, text="Informasi Pengguna", command=self.tampilkan_informasi_pengguna).grid(row=6, column=0, padx=5)
        tk.Button(main_frame, text="Tentang", command=self.tentang_menu).grid(row=7, column=0, padx=5)
        
    def tampilkan_daftar_penerima(self):
        daftar_penerima_message = self.dompet.get_daftar_penerima_menu()
        messagebox.showinfo("Daftar Penerima", daftar_penerima_message)

    def cek_saldo(self):
        saldo_message = self.dompet.cek_saldo()
        messagebox.showinfo("Saldo", saldo_message)

    def top_up(self):
        amount = simpledialog.askfloat("Top Up", "Masukkan jumlah top up:")
        if amount is not None:
            self.dompet.top_up(amount)
            saldo_message = f"Top up berhasil. Saldo sekarang: Rp. {self.dompet.saldo:,.2f}"
            messagebox.showinfo("Top Up Berhasil", saldo_message)

    def tarik_uang_gui(self):
        amount = simpledialog.askfloat("Tarik Uang", "Masukkan jumlah penarikan:")
        if amount is not None:
            result_message = self.dompet.tarik_uang_gui(amount)
            messagebox.showinfo("Penarikan Berhasil", result_message)

    def transfer_gui(self):
        target_username = simpledialog.askstring("Transfer", "Masukkan nama pengguna penerima:")
        amount = simpledialog.askfloat("Transfer", "Masukkan jumlah transfer:")
        if target_username is not None and amount is not None:
                result_message = self.dompet.transfer(target_username, amount)
                messagebox.showinfo("Transfer Berhasil", result_message)
        else:
                messagebox.showerror("Transfer Gagal", "Penerima dengan nama pengguna tersebut tidak ditemukan.")

    def pengaturan_menu(self):
        sub_menu = tk.Toplevel(self)
        sub_menu.title("Pengaturan")

        tk.Button(sub_menu, text="Ganti Nama Pengguna", command=self.ganti_username).pack(pady=10)
        tk.Button(sub_menu, text="Ganti Password", command=self.ganti_password).pack(pady=10)
        tk.Button(sub_menu, text="Ubah Informasi Pengguna", command=self.ubah_informasi_pengguna_gui).pack(pady=10)

    def ganti_username(self):
        new_username = simpledialog.askstring("Ganti Nama Pengguna", "Masukkan nama pengguna baru:")
        if new_username is not None:
            # Update the username in the DompetDigital object
            self.dompet.username = new_username
            messagebox.showinfo("Ganti Nama Pengguna", "Nama pengguna berhasil diubah!")

    def ganti_password(self):
        new_password = simpledialog.askstring("Ganti Password", "Masukkan password baru:")
        if new_password is not None:
            # Update the password in the DompetDigital object
            self.dompet.password = new_password
            messagebox.showinfo("Ganti Password", "Password berhasil diubah!")

    def ubah_informasi_pengguna_gui(self):
        new_info = simpledialog.askstring("Ubah Informasi Pengguna", "Masukkan informasi pengguna baru:")
        if new_info is not None:
            result_message = self.dompet.ubah_informasi_pengguna(new_info)
            messagebox.showinfo("Ubah Informasi Pengguna", result_message)

    def tampilkan_informasi_pengguna(self):
        info_message = self.dompet.tampilkan_informasi_pengguna()
        messagebox.showinfo("Informasi Pengguna", info_message)

    def tentang_menu(self):
        tentang_message = self.dompet.tentang_menu()
        messagebox.showinfo("Tentang", tentang_message)

    def get_dompet_by_username(self, target_username):
        # Implementasikan logika untuk mendapatkan objek DompetDigital berdasarkan username.
        # Misalnya, jika ada daftar objek DompetDigital, Anda dapat mencari objek dengan username yang sesuai.
        # Fungsi ini harus mengembalikan objek DompetDigital atau None jika tidak ditemukan.
        return None

if __name__ == "__main__":
    dompet = DompetDigital()
    dompet_gui = DompetDigitalGUI(dompet)
    dompet_gui.mainloop()
