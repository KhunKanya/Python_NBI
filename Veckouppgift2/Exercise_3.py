#Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.

tottenham = int(input("Hur många mål gjorde Tottenham?: "))
liverpool = int(input("Hur många mål gjord Liverpool?: "))
# version 1 & 3.  Se vilket lag som gjorde flest matcher,
# och skriver ut vem som vann med hur många mål. Oavgjort om resultatet är samma

if tottenham > liverpool:
    print("Tottenham vann med " + str(tottenham - liverpool) + " mål!")
elif liverpool > tottenham:
    print("Liverpool vann med " + str(liverpool - tottenham) + " mål!")
else:
    print("matchen blev lika")

#Version 2: programmet ska tala om ifall det blev oavgjort.

# if tottenham == liverpool:
#     print("Matchen blev oavgjord")
# elif tottenham > liverpool:
#     print("Tottenham vann!")
# else:
#     print("Liverpool vann!")

#Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
#Tottenham vann med 1 mål!

