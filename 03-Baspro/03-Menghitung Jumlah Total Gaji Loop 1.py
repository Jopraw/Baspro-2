nama = input("Masukkan Nama: ")
nik = input("Masukkan NIK: ")

status_list = ["pegawai tetap", "honor"]
golongan_list = ["A", "B", "C"]

gaji_pokok_list = {
    "pegawai tetap": 1000000,
    "honor": 750000
}

bonus_list = {
    "A": {"pegawai tetap": 200000, "honor": 150000},
    "B": {"pegawai tetap": 400000, "honor": 275000},
    "C": {"pegawai tetap": 600000, "honor": 480000}
}

total_salary = {"pegawai tetap": 0, "honor": 0}

print("\n=== Daftar Gaji dan Bonus ===")
print("Nama:", nama)
print("NIK:", nik, "\n")

for status in status_list:
    for golongan in golongan_list:
        gaji_pokok = gaji_pokok_list[status]
        bonus = bonus_list[golongan][status]
        gaji_total = gaji_pokok + bonus
        total_salary[status] += gaji_total
        
        print("=== Rincian Gaji ===")
        print("Status      :", status.capitalize())
        print("Golongan    :", golongan)
        print("Gaji Pokok  : Rp", format(gaji_pokok, ","))
        print("Bonus       : Rp", format(bonus, ","))
        print("Gaji Total  : Rp", format(gaji_total, ","), "\n")

print("\n=== Total Gaji + Bonus untuk Setiap Status ===")
for status, total in total_salary.items():
    print(status.capitalize(), ": Rp", format(total, ","))
