# Document type aniqlash.   
import os

fayl_nomi = input("Fayl nomini kiriting: ")
fayl_turi = os.path.splitext(fayl_nomi)[1].lower()

ruxsat_etilgan = ['.pdf', '.docx', '.txt']

#natija
print(fayl_turi in ruxsat_etilgan)

