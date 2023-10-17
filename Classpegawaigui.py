import tkinter as tk
from tkinter import messagebox

class Pegawai:
    def _init_(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def tampilkan_data(self):
        return f"Nama: {self.nama}\nGaji: {self.gaji}"


class PegawaiTetap(Pegawai):
    def _init_(self, nama, gaji, tunjangan):
        super()._init_(nama, gaji)
        self.tunjangan = tunjangan

    def tampilkan_data(self):
        return super().tampilkan_data() + f"\nTunjangan: {self.tunjangan}"


class PegawaiHarian(Pegawai):
    def _init_(self, nama, gaji_per_hari, jumlah_hari):
        super()._init_(nama, 0)  # Gaji awal diatur menjadi 0 untuk pegawai harian
        self.gaji_per_hari = gaji_per_hari
        self.jumlah_hari = jumlah_hari

    def hitung_gaji(self):
        self.gaji = self.gaji_per_hari * self.jumlah_hari

    def tampilkan_data(self):
        return super().tampilkan_data() + f"\nGaji per Hari: {self.gaji_per_hari}\nJumlah Hari Kerja: {self.jumlah_hari}\nGaji Total: {self.gaji}"


class PegawaiKontrak(Pegawai):
    def _init_(self, nama, gaji_bulanan):
        super()._init_(nama, gaji_bulanan)

    def tampilkan_data(self):
        return super().tampilkan_data()


def tampilkan_info_pegawai():
    nama = entry_nama.get()
    gaji = float(entry_gaji.get())

    if var_jenis_pegawai.get() == 1:
        tunjangan = float(entry_tunjangan.get())
        pegawai = PegawaiTetap(nama, gaji, tunjangan)
    elif var_jenis_pegawai.get() == 2:
        gaji_per_hari = float(entry_gaji_per_hari.get())
        jumlah_hari = float(entry_jumlah_hari.get())
        pegawai = PegawaiHarian(nama, gaji_per_hari, jumlah_hari)
        pegawai.hitung_gaji()  # Hitung gaji untuk pegawai harian
    else:
        pegawai = PegawaiKontrak(nama, gaji)

    info_pegawai = pegawai.tampilkan_data()
    messagebox.showinfo("Informasi Pegawai", info_pegawai)


# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Informasi Pegawai")

# Label dan Entry untuk Nama
label_nama = tk.Label(root, text="Nama Pegawai:")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

# Label dan Entry untuk Gaji
label_gaji = tk.Label(root, text="Gaji Pegawai:")
label_gaji.grid(row=1, column=0)
entry_gaji = tk.Entry(root)
entry_gaji.grid(row=1, column=1)

# Pilihan jenis pegawai
var_jenis_pegawai = tk.IntVar()
label_jenis = tk.Label(root, text="Jenis Pegawai:")
label_jenis.grid(row=2, column=0)

radio_tetap = tk.Radiobutton(root, text="Pegawai Tetap", variable=var_jenis_pegawai, value=1)
radio_tetap.grid(row=2, column=1)

radio_harian = tk.Radiobutton(root, text="Pegawai Harian", variable=var_jenis_pegawai, value=2)
radio_harian.grid(row=2, column=2)

radio_kontrak = tk.Radiobutton(root, text="Pegawai Kontrak", variable=var_jenis_pegawai, value=3)
radio_kontrak.grid(row=2, column=3)

# Entry untuk data tambahan (tunjangan, gaji per hari, jumlah hari)
label_tunjangan = tk.Label(root, text="Tunjangan:")
label_tunjangan.grid(row=3, column=0)
entry_tunjangan = tk.Entry(root)
entry_tunjangan.grid(row=3, column=1)

label_gaji_per_hari = tk.Label(root, text="Gaji per Hari:")
label_gaji_per_hari.grid(row=4, column=0)
entry_gaji_per_hari = tk.Entry(root)
entry_gaji_per_hari.grid(row=4, column=1)

label_jumlah_hari = tk.Label(root, text="Jumlah Hari Kerja:")
label_jumlah_hari.grid(row=5, column=0)
entry_jumlah_hari = tk.Entry(root)
entry_jumlah_hari.grid(row=5, column=1)

# Tombol untuk menampilkan informasi pegawai
button_tampilkan = tk.Button(root, text="Tampilkan Informasi Pegawai", command=tampilkan_info_pegawai)
button_tampilkan.grid(row=6, column=0, columnspan=4)

root.mainloop()