# BMI hisoblash va tansif.
vazn = float(input("Vazn (kg): "))
boy = float(input("Bo'y (m): "))

# Ma'lumotlarni tekshiramiz
if vazn <= 0 or boy <= 0:
    print("Xatolik: Vazn va bo'y musbat bo'lishi kerak.")
elif not (0.5 <= boy <= 3.0):
    print("Xatolik: Bo'y 0.5 dan 3.0 metrgacha bo'lishi kerak.")
elif not (1 <= vazn <= 500):
    print("Xatolik: Vazn 1 dan 500 kg gacha bo'lishi kerak.")
else:
    # Hisoblaymiz
    bmi = vazn / (boy ** 2)
    print("BMI:", round(bmi, 2))
    
    # BMI ni tasniflaymiz
    if bmi < 18.5:
        print("Tasnif: Kam vazn")
    elif bmi < 25:
        print("Tasnif: Normal vazn")
    elif bmi < 30:
        print("Tasnif: Ortiqcha vazn")
    else:
        print("Tasnif: Semizlik")
