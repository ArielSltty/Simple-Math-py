# Ariel Siletty
# Nim : 202351057

print("***Perusahaan Boneka***")

x = int(input("Masukkan jumlah boneka yang ingin dibeli: "))

if x < 1:
    print("Jumlah boneka harus lebih dari 0")
else:
    if x <= 12:
        harga_per_boneka = 20000
    elif x <= 24:
        harga_per_boneka = 19500
    elif x <= 50:
        harga_per_boneka = 18000
    else:
        harga_per_boneka = 17000

    harga_total = x * harga_per_boneka
    print(f"Harga boneka Rp {harga_per_boneka}")
    print(f"Total harga Rp {harga_total}")