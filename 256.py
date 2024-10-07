# List untuk menyimpan hasil
results = []
counter = 1

# Loop untuk semua kombinasi LN, LE, LS, LW dari 0 sampai 4
for LW in range(1, 5):
    for LS in range(1, 5):
        for LE in range(1, 5):
            for LN in range(1, 5):
                # Hitung nilai dari tingkat Kemacetan
                result_LN = (2**0 * LN)
                result_LE = (2**1 * LE)
                result_LS = (2**2 * LS)
                result_LW = (2**3 * LW)
                # Rumus Kedua membuat tidak ada satupun nilai hasil yang sama
                result = (2**0 * result_LN) + (2**1 * result_LE) + (2**2 * result_LS) + (2**3 * result_LW)

                # Simpan hasilnya dalam list sebagai tuple
                results.append((counter, LN, LE, LS, LW, result))
                counter += 1  # Increment counter

# Cetak hasil
for r in results:
    print(f"{r[0]}. LN={r[1]}, LE={r[2]}, LS={r[3]}, LW={r[4]}: Result={r[5]}")
