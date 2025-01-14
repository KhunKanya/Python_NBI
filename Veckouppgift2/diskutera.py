is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
member_check = int(input("Om du är medlem, skriv 1: "))
if member_check == 1:
    is_member = True
price = float(price)
if is_member:
    if price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
        discount = discount + 25
    elif price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
        discount = discount + 10
    else:
        print("För billigt, ingen rabatt!")
else:
    print("Du är inte medlem, du måste betala fullt pris!")
final_price = price * (100 - discount) / 100
print("Efter rabatter blir priset.... " + str(final_price))