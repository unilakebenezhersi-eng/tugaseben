from data_pengeluaran import tambah_pengeluaran, tampilkan_pengeluaran, ambil_data
import analisis

def menu():
    while True:
        print("\n====== MONITORING PENGELUARAN HARIAN ======")
        print("1. Tambah Data Pengeluaran")
        print("2. Lihat Semua Pengeluaran")
        print("3. Lihat Ringkasan & Saran")
        print("4. Keluar")
        pilih = input("Pilih menu (1-4): ")

        if pilih == "1":
            nama = input("Masukkan nama pengeluaran: ")
            try:
                jumlah = int(input("Masukkan jumlah (Rp): "))
                tambah_pengeluaran(nama, jumlah)
                print("Pengeluaran berhasil dicatat!")
            except ValueError:
                print("Input jumlah harus berupa angka.")
        elif pilih == "2":
            tampilkan_pengeluaran()
        elif pilih == "3":
            data = ambil_data()
            total = analisis.total_pengeluaran(data)
            terbesar = analisis.pengeluaran_terbesar(data)
            print(f"\nTotal Pengeluaran Hari Ini: Rp {total}")
            if terbesar:
                print(f"Pengeluaran terbesar: {terbesar['nama']} - Rp {terbesar['jumlah']}")
            print(analisis.saran_penghematan(total))
        elif pilih == "4":
            print("Terima kasih telah menggunakan program Monitoring Pengeluaran!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    menu()