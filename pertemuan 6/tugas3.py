belanja = [
    {"produk":"baju","jumlah":20},
    {"produk": "celana", "jumlah":15},
    {"produk": "sepatu", "jumlah":25},
]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["jumlah"]

    print("total belanjaan : ", total_belanjaan)