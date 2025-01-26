Veckouppgift 3
Vecka 3, 20/1
1

4 Vad skrivs ut?
För att förstå koden kan du sätta ut brytpunkter och köra med debugging. Det kan också underlätta att skriva samtidigt med papper och penna.

2 Öva på loopar och listor
1a Skriv färdigt kodexemplet.
answer = 0
for i in ????????????:
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)

1c Skriv om 1b så att den använder en while-loop.


2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3] 


3 Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
3b Lägg till "Fellowship of the ring" sist i listan.
3c Lägg till "The two towers" på första platsen i listan. (index noll)
3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
3f Ta reda på hur lång listan är. (len)
3g Vänd listan baklänges.
3h Sortera listan stigande i bokstavsordning.

Kom ihåg att göra code review!

3 Kvittouträknaren
Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen. Exempel:
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 25
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Det blir 75 kr totalt. Välkommen åter!

Tips! För att lösa uppgiften behöver du: flera variabler, input, while-loop.

Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
Hur många är ni? 3
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!

Version 3: programmet ska fråga hur många procent dricks man vill lägga på. Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.

Nice to have: prova att använda try+except eller isdigit för att hantera de fall när användaren skriver ett felaktigt värde. Python Try Except , isdigit | StackOverflow 
("Nice to have" handlar om funktionalitet som inte är nödvändig, men som är bra att ha. Gå gärna vidare till nästa uppgift och återvänd till den här om du vill lära dig mer.)

Testa programmet med följande inputs:
Version 1:
100
10, 20, 15

Version 2:
100, 1 person
100, 2 personer
10, 10, 40 personer
30, 20, 30, 1 person

Lägg till egna testfall för dricksen.

Kom ihåg att göra code review!

4 Figurer med loopar
Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

a-f

g-j


5 Gissa talet
Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa det. Om man gissar för lågt eller för högt ska spelet tala om det. Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
secret = random.randint(1, 100)

Exempel:
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
Gissa: 40
Nej, det är för lågt!
Gissa: 55
Nej, det är för högt!
Gissa: 51
Det är rätt!! Du gjorde det på 3 gissningar.

Version 2: skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
"Nu börjar det brännas!"


6 Todo list (att göra-lista)
Bygg ett program där användaren kan lägga till saker till en todo-lista.
Tips: använd en loop, input och en variabel för listan.
Exempel:

** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
Välj ett alternativ: 1
Din lista är tom
.
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: mata guldfisken
Ok, lade till "mata guldfisken" i listan.
.
Välj ett alternativ: 1
+ Mata guldfisken
.

Version 2: lägg till ett menyalternativ, "Markera som klar". När användaren väljer det, ska programmet fråga efter vilken grej man är färdig med. Den färdiga grejen ska tas bort från listan.

Version 3: lägg över färdiga grejer i en ny lista. Användaren ska kunna välja vad man har bockat av tidigare, eller välja att lägga tillbaka grejen i todo-listan.


Vad är code review?
Alla i gruppen visar i tur ordning upp hur långt man har kommit med uppgiften. När man inte visar, har man som uppgift att ge konstruktiv feedback. Observera att man inte behöver vara färdig! Code review kan vara ett mycket bra stöd för att komma vidare.

Den som visar upp sin kod:
Kör programmet (oavsett om det blir fel eller inte)
Visar upp kodfilerna

De som ger feedback:
Frågar om det är något man inte förstår
Ger förslag på hur koden kan förbättras

.
