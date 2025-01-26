# Veckouppgift 1
  Vecka 2, 8/1

---
## 1 Skapa projekt och synka med GitHub
1 Skapa ett nytt Python-projekt, med ett git-repository. Skapa en fil med namnet "main.py". När man kör filen ska programmet skriva ut följande på terminalen, fast byt ut "Ditt Namn" mot ditt namn:
```bash
"Hello world"
"This program was made by Ditt Namn"
```
2 Lägg till alla ändringar till en commit.

3 Öppna inställningarna: File → Settings → Version Control → GitHub. Lägg till ditt GitHub-konto.

4 Klicka på main-branch-ikonen. Välj alternativet "Push" och "Define remote".

5 Skapa ett repository på GitHub. Se till att det är public. Kopiera URL till repot (webbläsarens adressfält) och skriv in i fältet "Define remote". Nu kan du synka ditt lokala projekt med remote som är GitHub. Det gör det lätt att dela din kod mellan olika datorer.

----
## 2 Diskutera i grupp
Rätta eventuella fel. Vad gör koden.
```bash
x = 100  # biljettpris
y = 200  # pengar på fickan
print("Det blir " + (y - x) " kronor över.")
z = 200 - 100 / 2
print("Hälften är: " + z)
```
Kom på bättre namn, i stället för x, y och z.
## 3 Använda variabler och datatyper
1a Använd input för att be användaren om ett heltal. Spara värdet i en variabel. Omvandla variabelns värde till ett heltal, och skriv ut det för att testa om du har gjort rätt.
Kodexempel med input:
```python
x = input("Fråga här")
```
1b Fråga användaren efter ett annat heltal. Skriv ut summan av talen, alltså tal1 + tal2.
Testa genom att hitta på två tal och räkna ut summan i huvudet. Kontrollera om programmet räknar rätt.

2a Nu är det dags att köpa vinterkläder. Du ser en fin jacka som kostar 2000 kronor. Jackan är på rea, 50%. Skriv ett program som räknar ut hur mycket du behöver betala.
Tips: 
```python
räkna ut rabatten med formeln: slut_pris = pris * rea_procent / 100.
```

2b Gör om programmet så att användaren kan skriva in en procentsats.
Testa genom att hitta på en procentsats och räkna ut vad programmet ska svara med, innan du kör det. 
```python
Till exempel 10%, som är 200 kr. Då ska jackan kosta 2000 - 200 == 1800 kr.
```

------

## 4 Fler övningar
1a Det är ca 470 km mellan Stockholm och Göteborg. Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. Du behöver fråga användaren hur fort man ska köra, i km/h.
```bash
Tips: omvandla till m/s genom att dela med 3,6. Sedan kan du använda formeln: tid = sträcka / hastighet.
```
1b Gör så att programmet svarar i minuter i stället för timmar.

1c (svårare) Nu ska programmet svara i hela timmar och minuter.
Tips: använd operatorerna // och %. Heltalsdivision // dividerar och avrundar nedåt till närmaste heltal. Procent % räknar ut resten vid division med heltal. 

Exempel:
```python
3 // 2 == 1      (3 / 2 == 1.5, avrundar nedåt)
60 % 60 == 0  (ingen rest)
70 % 60 == 10  (10 i rest)
```
Be en AI förklara heltalsdivision och modulo i Python om du känner dig osäker!

2 Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. Användaren behöver skriva in längden på de två kortare sidorna.
Tips 1: fråga en AI om formeln Pythagoras sats. Men var noga med att inte fråga efter kod som löser uppgiften!

Tips 2: räkna ut roten med math.sqrt().

3a Skriv ett program som talar om dagens datum.
Resurs: [Hantera datum i Python ](https://www.programmerapython.se/datum-i-python/) 

3b (svårare) Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.

-----

## Vad är code review?
Alla i gruppen visar i tur ordning upp hur långt man har kommit med uppgiften. När man inte visar, har man som uppgift att ge konstruktiv feedback. Observera att man inte behöver vara färdig! Code review kan vara ett mycket bra stöd för att komma vidare.

Den som visar upp sin kod:
1. Kör programmet (oavsett om det blir fel eller inte)
Visar upp kodfilerna.
2. Visar upp kodfilerna.

De som ger feedback:
1. Frågar om det är något man inte förstår.
2. Ger förslag på hur koden kan förbättras.




