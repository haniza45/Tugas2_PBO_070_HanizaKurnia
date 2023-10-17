class Pegawai:
    def __init__(self, id, nama, gaji):
        self.id = id
        self.nama = nama
        self.gaji = gaji

    def getNama(self):
        return self.nama

    def getGaji(self):
        return self.gaji

    def setGaji(self, gaji):
        self.gaji = gaji

    def info(self):
        print(f"ID Pegawai: {self.id}")
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")


class PegawaiTetap(Pegawai):
    def __init__(self, id, nama, gaji, tunjangan):
        super().__init__(id, nama, gaji)
        self.tunjangan = tunjangan

    def getTunjangan(self):
        return self.tunjangan

    def info(self):
        super().info()
        print(f"Tunjangan: {self.tunjangan}")


class PegawaiHarian(Pegawai):
    def __init__(self, id, nama, gaji, jam_kerja, tarif_per_jam):
        super().__init__(id, nama, gaji)
        self.jam_kerja = jam_kerja
        self.tarif_per_jam = tarif_per_jam

    def hitungGaji(self):
        return self.gaji + (self.jam_kerja * self.tarif_per_jam)

    def info(self):
        super().info()
        print(f"Jam Kerja: {self.jam_kerja}")
        print(f"Tarif per Jam: {self.tarif_per_jam}")


class PegawaiKontrak(Pegawai):
    def __init__(self, id, nama, gaji, durasi, tarif):
        super().__init__(id, nama, gaji)
        self.durasi = durasi
        self.tarif = tarif

    def hitungGaji(self):
        return self.gaji + (self.durasi * self.tarif)

    def info(self):
        super().info()
        print(f"Durasi Kontrak: {self.durasi}")
        print(f"Tarif: {self.tarif}")


# Contoh penggunaan
pegawai_tetap = PegawaiTetap(1, "John Doe", 5000, 1000)
pegawai_harian = PegawaiHarian(2, "Jane Smith", 0, 40, 20)
pegawai_kontrak = PegawaiKontrak(3, "Bob Johnson", 3000, 6, 500)

pegawai_tetap.info()
print("Total Gaji Pegawai Tetap:", pegawai_tetap.hitungGaji())
print()

pegawai_harian.info()
print("Total Gaji Pegawai Harian:", pegawai_harian.hitungGaji())
print()

pegawai_kontrak.info()
print("Total Gaji Pegawai Kontrak:", pegawai_kontrak.hitungGaji())
