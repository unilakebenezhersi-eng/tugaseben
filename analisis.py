"""
Modul Analisis Pengeluaran
Untuk menghitung total, terbesar, dan saran penghematan
"""

def total_pengeluaran(data):
    return sum(item['jumlah'] for item in data)

def pengeluaran_terbesar(data):
    if not data:
        return None
    return max(data, key=lambda item: item['jumlah'])

def saran_penghematan(total):
    batas = 100000
    if total > batas:
        return f"Pengeluaran hari ini Rp {total} cukup besar, coba kurangi belanja yang kurang penting besok."
    else:
        return "Pengeluaran Anda masih dalam batas aman. Tetap pertahankan ya!"