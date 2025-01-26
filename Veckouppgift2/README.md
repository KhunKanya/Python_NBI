# Veckouppgift 2
Vecka 3, 13/1

## 2 Balder
För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!

1. Fråga användaren hur lång man är (i cm)
2. Skriv ut antingen "Du får åka!" eller "Du får inte åka"

Skriv in följande värden för att testa att ditt program gjort rätt:
1. 121 cm (får inte åka)
2. 130 cm (får åka)
3. 155 cm (får åka)


Diskutera:
- Varför just tre värden?
- Varför dessa värden?
- Skulle det vara bra att lägga till testvärdet 129 cm?

## 3 Sportresultat
Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.
Exempel på output:
```python
Matchen är över, nu ska vi räkna ut resultatet!
Hur många mål gjorde Tottenham? 2
Hur många mål gjorde Liverpool? 1
Tottenham vann!
```

Version 2: programmet ska tala om ifall det blev oavgjort.

Version 3: nu ska programmet tala om hur många mål mer laget vann med. Exempel:
```python
Tottenham vann med 1 mål!
```
Eftersom det finns tre möjliga utfall (lag 1 vinst, lag 2 vinst, oavgjort) behöver du minst tre testfall. Hitta på värden som du kan använda för att testa alla möjliga utfall.

-----
## 4 Temperaturomvandling
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:
```bash
Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.
```
Version 2: fråga först användaren om man vill ange temperaturen i Celsius eller Fahrenheit. Sedan räknar programmet om till den andra temperaturen.
```bash
Tips: be användaren skriva in t.ex. "F" om man vill ange temperaturen i i Fahrenheit. Använd sedan if + else.
```

Version 3: om temperaturen som omvandlas är under 10°C ska programmet dessutom säga till användaren att ta på sig vinterkläder. Och om temperaturen är minst 20°C ska det föreslå att man packar badkläder.
```python
Formel för konvertering mellan temperaturenheter:
C = (F - 32) / 1.8
F = 1.8 * C + 32
```
Förslag på värden att testa med:

° Celsius| ° Fahrenheit |
--- |-----|
0 | 32  |
-17.777 | 0   |
37.777 | 100 |
100 | 212 |

----

## 5 Miniräknare

1 Gör ett program som frågar användaren efter 3 tal. Sedan ska det räkna ut vad summan blir, och skriva ut på konsolen. (summa: tal1 + tal2 + tal3)

2 Programmet ska tala om vilket som är det största talet, utan att använda Python-funktionen max. Använd i stället if/elif/else. Fundera på om man kan lösa uppgiften på olika sätt.

3 Programmet ska tala om ifall två av talen är lika, eller alla tre är lika.

4 Programmet ska tala om vilket som är det mellersta talet. Observera att det bara finns ett mellersta tal om alla tre är olika, eller alla tre är lika. (Om talen skulle vara till exempel 2, 2, 5 så räknas inget av dem som mellerst i den här uppgiften.)

För att testa systematiskt kan du göra en tabell. Kör sedan programmet. Kontrollera att programmet skriver ut samma saker som du har skrivit in i tabellen. Vi kallar talen t1, t2 och t3.
Förslag på värden att testa med:  1 2 3, 1 3 2, 3 2 1, -1 -3 -1, 9 9 9, 32 32 16


| t1  | t2  | t3  | Störst | Två lika? | Tre lika? | Mellerst? | 
|:---:|:---:|:---:|:------:|:---------:|:---------:|:---------:| 
|  1  |  2  |  3  |   3    |     nej      |    nej    | 2


----

## Vad är code review?
Alla i gruppen visar i tur ordning upp hur långt man har kommit med uppgiften. När man inte visar, har man som uppgift att ge konstruktiv feedback. Observera att man inte behöver vara färdig! Code review kan vara ett mycket bra stöd för att komma vidare.

Den som visar upp sin kod:
1. Kör programmet (oavsett om det blir fel eller inte)
Visar upp kodfilerna.
2. Visar upp kodfilerna.

De som ger feedback:
1. Frågar om det är något man inte förstår.
2. Ger förslag på hur koden kan förbättras.

