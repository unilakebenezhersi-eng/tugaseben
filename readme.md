# Monitoring Pengeluaran Harian (Modularisasi Python)

Program ini merupakan contoh **modularisasi program Python** untuk studi kasus pelacakan pengeluaran harian. Program dibagi menjadi beberapa modul agar lebih rapi, mudah dikembangkan, dan setiap bagian punya tanggung jawab jelas.

---

## Studi Kasus

**Permasalahan:**  
Banyak orang kesulitan mengontrol pengeluaran hariannya karena tidak pernah mencatat ataupun menganalisis belanja sehari-hari. Akibatnya, uang habis sebelum waktunya tanpa disadari. Program sederhana ini membantu pengguna mencatat setiap pengeluaran, menganalisis total pengeluaran, mencari pengeluaran terbesar, dan memberi saran untuk penghematan.

---

## Struktur Proyek

```
monitor_pengeluaran/
├── main.py                # Program utama/menu interaktif
├── data_pengeluaran.py    # Modul untuk catat dan tampil data pengeluaran
├── analisis.py            # Modul analisis (total, terbesar, saran)
└── README.md              # Dokumentasi
```

---

## Penjelasan Modul

- **data_pengeluaran.py**  
  Menyimpan, mengambil, dan menampilkan data pengeluaran harian dalam bentuk list of dict.

- **analisis.py**  
  Menghitung total pengeluaran, menemukan kategori terbesar, dan memberi saran sederhana.

- **main.py**  
  Program utama yang mengatur menu, input user, dan interaksi dengan kedua modul di atas.

---

## Cara Menjalankan Program

1. **Pastikan semua file disimpan dalam satu folder.**
2. **Buka terminal/command prompt pada folder tersebut.**
3. **Jalankan program utama:**
   ```bash
   python main.py
   ```
4. **Ikuti instruksi di layar untuk:**
   - Menambah data pengeluaran
   - Melihat seluruh pengeluaran harian
   - Melihat ringkasan dan saran

---

## Contoh Penggunaan

- **Tambah Data:**  
  Masukkan nama item (misal: "Jajan kopi") dan jumlah (misal: 18000).

- **Ringkasan:**  
  Program akan menampilkan total pengeluaran, pengeluaran terbesar hari itu, dan saran penghematan.

---

## Konsep Modularisasi yang Diterapkan

- **Setiap tugas dibagi dalam file berbeda (modul).**
- **Program utama hanya mengatur alur & menu.**
- **Fungsi dari modul diimpor dan dapat digunakan ulang.**

---

## Pengembang

Contoh studi kasus untuk modulasi Python (oleh Copilot GitHub, 2025).
