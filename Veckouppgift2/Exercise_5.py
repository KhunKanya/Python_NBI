#1 Gör ett program som frågar användaren efter 3 tal.
number1 = int(input("Skriv ett heltal: "))
number2 = int(input("Skriv ett hektal: "))
number3 = int(input("Skriv ett heltal: "))

summa = number1 + number2 + number3
#2 Programmet ska tala om vilket som är det största talet.
if number1 >= number2 and number1 >= number3:
    maximum = number1
elif number2 >= number1 and number2 >= number3:
    maximum = number2
elif number3 >= number1 and number3 >= number2:
    maximum = number3
else:
    maximum = "n/a"

print(f"Det största talet är {maximum}")

#3 Programmet ska tala om ifall två av talen är lika.
if number1 == number2 and number1 == number3:
    print("Alla talen är lika.")
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("Två av talen är lika.")

if number1 != number2 and number1 != number3 and number2 != number3:
    if (number1 > number2 and number1 < number3) or (number1 < number2 and number1 > number3):
        middle_num = number1
    elif (number2 > number1 and number2 < number3) or (number2 < number1 and number2 > number3):
        middle_num = number2
    else:
        middle_num = number3
    print(f"Det mellersta talet är {middle_num}")
else:
    print("Det finns inget mellersta tal i denna uppgift.")
