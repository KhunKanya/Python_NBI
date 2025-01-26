#3 Kvitto Räknaren.
# Gör ett program som upprepade gånger ber användaren skriva in ett tal.
print("Välkommen till Kvitto Kompis!")
total = 0

# while True:
#     user_action = input("Skriv in ett belopp:")
#     if user_action.isdigit():
#         total += int(user_action)
#         continue
#     elif user_action == "quit" or user_action == "avsluta":
#         print(f"Det blir {total}kr totalt. Welcome back")
#         break
#     else:
#         print("Invalid input. Please enter a number or quit/avsluta")
#         continue

#Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
guest_count = int(input("Hur många är ni?"))

# while True:
#     user_action = input("Skriv in ett belopp:")
#     if user_action.isdigit():
#         total += int(user_action)
#         continue
#     elif user_action == "quit" or user_action == "avsluta":
#         total_split = total / guest_count
#         print(f"Det blir {total}kr totalt, alltsa {total_split}kr per person. Welcome back")
#         break
#     else:
#         print("Invalid input. Please enter a number or quit/avsluta")
#         continue
#

# Version 3 programmet ska fråga hur många procent dricks man vill lägga på.

guest_tip = input("Hur mycket dricks vill du lägga på? ")

if len(guest_tip) == 0:
    guest_tip = 10
else:
    while True:
        try:
            guest_tip = int(guest_tip)
            break
        except ValueError:
            guest_tip = input("Du måste skriva en siffra: ")
            continue

while True:
    user_action = input("Skriv in ett belopp eller avsluta/quit:")
    if user_action.isdigit():
        total += int(user_action)
        continue
    elif user_action == "quit" or user_action == "avsluta":
        total_split = total / guest_count
        if guest_tip > 0:
            total = total + (total * guest_tip / 100)
            total_split = (total / guest_count)
        print(f"Det blir {total}kr totalt, alltsa {total_split}kr per person inklusive {guest_tip}% dricks. Welcome back!")
        break
    else:
        print("Invalid input. Please enter a number or quit/avsluta")
        continue
