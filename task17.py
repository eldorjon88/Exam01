# Baxolash tizimi.
ball = int(input("Iltimos, balingizni kiriting (0-100): "))

# Ball oraliqlariga qarab baho chiqaramiz
if 90 <= ball <= 100:
    print("A (A'lo)")
elif 80 <= ball <= 89:
    print("B (Yaxshi)")
elif 70 <= ball <= 79:
    print("C (Qoniqarli)")
elif 60 <= ball <= 69:
    print("D (Qoniqarsiz)")
elif 0 <= ball <= 59:
    print("F (Rad)")
else:
    print("Noto'g'ri ball kiritildi. Iltimos, 0 dan 100 gacha bo'lgan son kiriting.")
