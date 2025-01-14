# För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!
#1 Fråga användaren hur lång man är (i cm)
# Skriv ut antingen "Du får åka!" eller "Du får inte åka"

user = int(input("Hur lång du är? "))

#check if user is tall than 130 cm
if user >= 130:
    print("Du får åka!")
else:
    print("Du får inte åka")
