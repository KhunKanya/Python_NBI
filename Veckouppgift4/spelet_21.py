#Skriv en funktion som skriver ut det första talet i talserien som är större än 21.
def find_first_number_above():
    total = 0
    number = 1
    while total <= 21:
        total += number
        number += 1
    return number - 1  # Vi returnerar det sista talet som lades till

result = find_first_number_above()
print("Det första talet i serien vars summa överstiger 21 är:", result)


#Version2 : i stället för att använda talserien, slumpa tal mellan 1 och 13.
import random
def find_first_random_number_above():
    total = 0
    while total <= 21:
        card = random.randint(1, 13)
        total += card
        print(f"Slumpat kort: {card}, Total summa: {total}")
    return total

result = find_first_random_number_above()
print("Den totala summan som överstiger 21 är:", result)




#####    Vidareutveckling: Spelet 21 med användaren och datorn  ########
# import random
#
# def draw_card():
#     return random.randint(1, 13)
#
# def play_game():
#     player_total = 0
#     computer_total = 0
#
#     while True:    #spelarens tur
#     choice = input("Vill du ta ett nytt kort? (ja / nej): ").lower()
#     if choice == 'ja':
#         card = draw_card()
#         player_total += card
#         print(f"Du drog ett {card}. Din totala summa är nu {player_total}.")
#         if play_total > 21:
#             print("Du förlorade! Din summa överstiger 21.")
#             return
#     else:
#         break
#
# # Datorns tur
# while computer_total < 17:
#     card = draw_card()
#     computer += card
#     print(f"Datorn drog ett {card}. Datorns totala summa är nu {computer_total}.")
#     if computer_total > 21:
#         print("Datorn förlorade!")
#         return
#
# # Jämför resultat
# if player_total > computer_total:
#     print(f"Du vann! Dinn summa: {player_total}, Datorns summa: {computer_total}.")
# elif player_total < computer_total:
#     print(f"Datorn vann! Din summa: {player_total}, Datorn summa: {conputer_total}.")
# else:
#     print(f"Det blev oavgjort! Båda har summan {player_total}.")
#
# #starta spelet
# play_game()