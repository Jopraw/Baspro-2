AGE = int(input("Masukan Umur "))
if AGE <= 5:
    print("Termasuk Balita")
    
elif AGE > 5 and AGE <= 13:
    print("Termasuk Anak-Anak")

elif AGE > 13 and AGE <= 25:
    print("Termasuk Remaja")

elif AGE > 25 and AGE <= 35:
    print("Termasuk Dewasa")

elif AGE > 35 and AGE <= 55:
    print("Termasuk Orang Tua")

else:
    print("Termasuk Lansia")
(input("Press Any Key to Exit"))