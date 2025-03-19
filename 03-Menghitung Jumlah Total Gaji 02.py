# 1. Buat inputan, Nama, Nik, Status (Pegawai Tetap/Honor), Golongan (A/B/C)
# 2. Status Pegawai Tetap, Gaji 1.000.000, Bonus Golongan A, 200.000, B 400.000, C 550.000
# 3. Status Pegawai Honor, Gaji 750.000, Bonus Golongan A 150.000, B 275.000, C 480.000
# 4. Print Gaji, Bonus, dan Gaji Total
# 5. status dan golongan merupakan inputan String
NIK = int(input("Masukan NIK: "))
Nama = input("Masukan Nama: ")

# Loop untuk memastikan input status valid
while True:
    Status = input("Masukan Status (Pegawai Tetap/Honor): ")
    if Status in ["Pegawai Tetap", "Honor"]:
        break
    print("Status tidak valid, silakan masukkan kembali.")

# Loop untuk memastikan input golongan valid
while True:
    Golongan = input("Masukan Golongan (A/B/C): ")
    if Golongan in ["A", "B", "C"]:
        break
    print("Golongan tidak valid, silakan masukkan kembali.")

if Status == "Pegawai Tetap":
    Gaji = 1000000
    Bonus = {"A": 200000, "B": 400000, "C": 550000}[Golongan]
elif Status == "Honor":
    Gaji = 750000
    Bonus = {"A": 150000, "B": 275000, "C": 480000}[Golongan]

Gaji_Total = Gaji + Bonus

print("\n=== Data Karyawan ===")
print("Nama: ", Nama)
print("NIK: ", NIK)
print("Status: ", Status)
print("Golongan: ", Golongan)
print("Gaji: ", Gaji)
print("Bonus: ", Bonus)
print("Gaji Total: ", Gaji_Total)

input("Press any key to exit")