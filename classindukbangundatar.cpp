#include <iostream>

// Kelas Induk (Base Class)
class BangunDatar {
public:
    float luas;
    float keliling;
    
    void hitungLuas() {
        std::cout << "Menghitung luas bangun datar." << std::endl;
    }
    
    void hitungKeliling() {
        std::cout << "Menghitung keliling bangun datar." << std::endl;
    }
};

// Kelas Anak (Derived Class)
class PersegiPanjang : public BangunDatar {
public:
    float panjang;
    float lebar;
    
    void hitungLuas() {
        luas = panjang * lebar;
        std::cout << "Luas persegi panjang: " << luas << std::endl;
    }
    
    void hitungKeliling() {
        keliling = 2 * (panjang + lebar);
        std::cout << "Keliling persegi panjang: " << keliling << std::endl;
    }
};

int main() {
    PersegiPanjang pp;
    pp.panjang = 5.0;
    pp.lebar = 3.0;
    
    pp.hitungLuas(); // Memanggil metode dalam PersegiPanjang
    pp.hitungKeliling(); // Memanggil metode dalam PersegiPanjang
    
    // Memanggil metode dari kelas induk
    pp.BangunDatar::hitungLuas();
    pp.BangunDatar::hitungKeliling();
    
    return 0;
}
