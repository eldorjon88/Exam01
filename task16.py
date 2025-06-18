# Yoshga bog'liq chegirma.

# Chipta narxi
asosiy_narx = 1000

yosh = int(input("Yoshingizni kiriting: "))

# Chegirma hisoblash
if yosh < 7:
    chegirma = 0.5
elif 7 <= yosh <= 17:
    chegirma = 0.2
elif yosh > 60:
    chegirma = 0.3
else:
    chegirma = 0.0

# Yakuniy narx
yakuniy_narx = asosiy_narx * (1 - chegirma)

# Natijani chiqarish
print(f"Sizga {int(chegirma * 100)}% chegirma berildi.")
print(f"To'lashingiz kerak bo'lgan summa: {yakuniy_narx} so'm.")
