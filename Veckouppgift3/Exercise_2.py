# 2 Öva på loopar och listor
# answer = 0
# for i in range(1, 11):   # Lägg till range(1, 11):
#     answer += i
# print("Summan av talen 1 till 10 är: " + str(answer))  # Svaret ska bli 55

#1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)
# answer = 0
# for i in range(1, 101): # Lägg till range(1, 101):
#     answer += i
# print("summan av talen tal mellan 1 och 100 är: " + str(answer))  #svaret ska bli 5050

#1c Skriv om 1b så att den använder en while-loop.
# answer = 0
# i = 1
# while i <= 100:
#     answer += i
#     i += 1    # Öka i med 1 i varje iteration
# print("summan av talen tal mellan 1 och 100 är: " + str(answer))  #svaret ska bli 5050

#2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]
# lista = [1, -2, 3, -2, 4, -3]
# summan = 0
#
# for num in lista:
#     summan += num
# print(summan)

#3a Skapa en lista med namnen på fyra filmer.

filmer = ["Squid game", "Harry potter", "Mr.Bean's", "Star wars", "The monkey king"]
filmer.append("Fellowship of the ring")    # 3b: Lägg till "Fellowship of the ring" sist i listan

# for film in filmer:
#     print(film)
print("____________________")
filmer.insert(0, "the two towers")  #Lägg till "The two towers" på första platsen i listan. (index noll)
Hej = filmer.index("the two towers")
filmer.remove("Squid game")
print(f"two towers har index {Hej}")

print(filmer)
filmer.reverse()
filmer.sort()
print(filmer)
