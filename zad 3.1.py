s = input("Podaj wyrazy\n")

znaki = [".", "!", "?"]

male, duze, zdan = 0, 0, 0

for c in s:
    if c in znaki:
        zdan += 1
    o = ord(c)
    if o >= 65 and o <= 90:
        duze += 1
    if o >= 97 and o <= 122:
        male += 1

print ("w wyrazie znajduja sie", male, "malych liter")
print ("w wyrazie znajduja sie", duze, "duzych liter")
print ("w tekscie znajduje sie", zdan, "zdan")