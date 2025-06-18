#QQS bilan mahsulot narxini hisoblash (15%)
asosiy_narx = float(input("Mahsulotning asosiy narxini kiriting: "))
qqs_foiz = 15

#Hisoblash.
qqs_summasi = asosiy_narx * qqs_foiz / 100
umumiy_narx = asosiy_narx + qqs_summasi

#Natija.
print("QQS summasi:", qqs_summasi)
print("QQS bilan umumiy narx:", umumiy_narx)
