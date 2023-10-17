#include <iostream>
#include <cmath>

class BangunDatar {
public:
    virtual double hitungLuas() = 0;
};

class Persegi : public BangunDatar {
private:
    double sisi;

public:
    Persegi(double sisi) : sisi(sisi) {}

    double hitungLuas() override {
        return sisi * sisi;
    }
};

class PersegiPanjang : public BangunDatar {
private:
    double panjang;
    double lebar;

public:
    PersegiPanjang(double panjang, double lebar) : panjang(panjang), lebar(lebar) {}

    double hitungLuas() override {
        return panjang * lebar;
    }
};

class Lingkaran : public BangunDatar {
private:
    double jariJari;

public:
    Lingkaran(double jariJari) : jariJari(jariJari) {}

    double hitungLuas() override {
        return M_PI * jariJari * jariJari;
    }
};

class Segitiga : public BangunDatar {
private:
    double alas;
    double tinggi;

public:
    Segitiga(double alas, double tinggi) : alas(alas), tinggi(tinggi) {}

    double hitungLuas() override {
        return 0.5 * alas * tinggi;
    }
};

int main() {
    // Contoh penggunaan
    Persegi persegi(5);
    PersegiPanjang persegiPanjang(4, 6);
    Lingkaran lingkaran(3);
    Segitiga segitiga(4, 5);

    std::cout << "Luas Persegi: " << persegi.hitungLuas() << std::endl;
    std::cout << "Luas Persegi Panjang: " << persegiPanjang.hitungLuas() << std::endl;
    std::cout << "Luas Lingkaran: " << lingkaran.hitungLuas() << std::endl;
    std::cout << "Luas Segitiga: " << segitiga.hitungLuas() << std::endl;

    return 0;
}
