"""
Modul Data Pengeluaran
Menyimpan dan menampilkan data pengeluaran harian
"""

pengeluaran_harian = []

def tambah_pengeluaran(nama, jumlah):
    pengeluaran_harian.append({'nama': nama, 'jumlah': jumlah})

def ambil_data():
    return pengeluaran_harian

def tampilkan_pengeluaran():
    if not pengeluaran_harian:
        print("Belum ada data pengeluaran.")
    else:
        print("\nDaftar Pengeluaran Hari Ini:")
        for i, data in enumerate(pengeluaran_harian, 1):
            print(f"{i}. {data['nama']} - Rp {data['jumlah']}")