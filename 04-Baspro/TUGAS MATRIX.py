# Membuat matriks 5x5 dengan angka 1 hingga 25
matrix = [[num for num in range(row * 5 + 1, row * 5 + 6)] for row in range(5)]

# Menampilkan matriks
print("Matriks 5x5:")
for row in matrix:
    print(row)

# Contoh dua matriks 5x5 untuk perkalian
matrix_a = [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [9, 7, 5, 3, 1],
    [10, 8, 6, 4, 2],
    [5, 5, 5, 5, 5]
]

matrix_b = [
    [1, 0, 2, 0, 3],
    [0, 1, 0, 2, 0],
    [1, 0, 2, 0, 3],
    [0, 1, 0, 2, 0],
    [1, 0, 2, 0, 3]
]

# Perkalian matriks A x B
result = []
for i in range(5):
    row = []
    for j in range(5):
        total = sum(matrix_a[i][k] * matrix_b[k][j] for k in range(5))
        row.append(total)
    result.append(row)

# Menampilkan hasil perkalian
print("\nHasil perkalian matriks A x B:")
for row in result:
    print(row)
