# Tugas Bahasa Pemrograman 2 - Matriks 5x5
# Nama    : Jojo Prawinata Situmeang
# NIM     : 3337240060
# Tanggal : 17/04/2025

# Matriks A
matrix_a = [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [9, 7, 5, 3, 1],
    [10, 8, 6, 4, 2],
    [5, 5, 5, 5, 5]
]

# Matriks B
matrix_b = [
    [1, 0, 2, 0, 3],
    [0, 1, 0, 2, 0],
    [1, 0, 2, 0, 3],
    [0, 1, 0, 2, 0],
    [1, 0, 2, 0, 3]
]

# Menampilkan Matriks A
print("Matriks A:")
for row in matrix_a:
    print(row)

# Menampilkan Matriks B
print("\nMatriks B:")
for row in matrix_b:
    print(row)

# Perkalian Matriks A x B
hasil = []
for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += matrix_a[i][k] * matrix_b[k][j]
        baris.append(total)
    hasil.append(baris)

# Menampilkan Hasil Perkalian
print("\nHasil perkalian matriks A x B:")
for row in hasil:
    print(row)
