sayi = 100
deger = 1
for i in range(sayi):
    deger = deger * (i + 1)

print("100 sayısının faktöriyeli: ", deger)

sayi = str(deger)
toplam = 0
for rakam in sayi:
    toplam += int(rakam)

print("Sayının rakamları toplamı:", toplam)