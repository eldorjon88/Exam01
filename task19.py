# Stringdagi unli harflarni sanang.
matn = input("Matn kiriting: ")

unlilar = "aeiou AEIOU"

sana = 0

for harf in matn:
    if harf in unlilar:
        sana += 1

# Natija
print("Unli harflar soni:", sana)
