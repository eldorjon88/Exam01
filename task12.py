# Matnda ma’lum bir so‘zning boshlanish pozitsiyasini topish.
matn = input("Matnni kiriting: ")
soz = input("Qidirilayotgan so'zni kiriting: ")

# So‘zning boshlanishi
pozitsiya = matn.find(soz)

# Natijani chiqarish
if pozitsiya != -1:
    print(f"So'z matnda {pozitsiya}-indekstdan boshlanadi.")
else:
    print("So'z matnda topilmadi.")
