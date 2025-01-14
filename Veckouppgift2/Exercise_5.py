#1 Gör ett program som frågar användaren efter 3 tal.
tal1 = int(input("Skriv ett heltal: "))
tal2 = int(input("Skriv ett hektal: "))
tal3 = int(input("Skriv ett heltal: "))

summa = tal1 + tal2 + tal3
#2 Programmet ska tala om vilket som är det största talet.
if tal1 >= tal2 and tal1 >= tal3:
    maximum = tal1
elif tal2 >= tal1 and tal2 >= tal3:
    maximum = tal2
elif tal3 >= tal1 and tal3 >= tal2:
    maximum = tal3
else:
    maximum = "n/a"

print(f"Det största talet är {maximum}")

#3 Programmet ska tala om ifall två av talen är lika.
if tal1 == tal2 and tal1 == tal3:
    print("Alla talen är lika.")
elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
    print("Två av talen är lika.")


