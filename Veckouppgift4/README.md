# Veckouppgift 4
Vecka 4, 27/1
1. Du ska lösa uppgiften självständigt eller tillsammans med en annan student. Men vid minst ett tillfälle ska du göra code review i en grupp.
2. Du får ta hjälp av AI för att förklara koncept och lösa fel. Du får inte be AI lösa uppgiften åt dig direkt. Om du gör det, kommer du inte att lära dig grunderna, och inte kunna lösa svårare problem.
----

# 1 Läsa och förstå kod - diskutera i grupp
Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?

```python
1a
def foo(t):
    print("test")

foo("hej")

1b
def fun1(x, y):
    return x * y

print(3, 5)

1c
def fun1(x, y):
    return x * y

print(fun1(3, 5))

1d
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

1e
a = 5
def fun3(a):
    a += 1

a += 2
print(a)

1f
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)
```
1g Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
```python
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

1h
def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
```
1. En uppgift i tre delar:
   1. Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.
   2. Lista ut vad som ska vara det förväntade resultatet för de tre testlistorna.
   3. Rätta felen, så funktionen gör det den ska.

```python
def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])
```
---
## 2 Öva på funktioner och moduler
Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

1. Skriv en funktion som tar en sträng som parameter. När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
```python
my_function("David") → "David är en riktig hacker"
```
2. a Skriv en funktion med namnet "eko". När den anropas med en sträng ska den upprepa strängen, och skriva ut resultatet. Exempel:
```python
eko("hej") → skriver ut "hejhej"
```
2. b Lägg till en parameter "count", som avgör hur många ekon som ska skapas. Exempel:```python
```python
eko("hej", 3) → skriver ut "hejhejhej"
```
3. Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
```python
end = 5
y = 1
for x in range(1, 100):
    y *= 2
    # avsluta loopen med en if-sats här
print(y)
```
4. Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
```python
last([1, 2, 3]) → 3
```
5. Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
```python
cut_edges([1, 2, 3, 4]) → [2, 3]
```
6. Lös felen i koden.
```python
def increase(x):
    return x
    x += 1

print(increase(1))
```
7. Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal. Funktionen ska returnera medelvärdet. Till exempel så räknar man ut medelvärdet av 4 och 8 genom med formeln: (4 + 8) / 2, vilket blir 6.

```text
Tips: det kan vara enklare att använda fler variabler.
```
8. Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
```python
pretty_print(["a", "b", 3.14])
Listan har 3 element:
1. a
2. b
3. 3.14
```
-----
# Spelet 21
Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större. Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i talserien som är större än 21.

Version 2: i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
Tips: importera modulen random och använd funktionen randint för att slumpa tal. 
```text
Exempel: card = random.randint(1, 13)
```
Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna. (slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.

---

## Pokerhand
När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. 

```python
poker_hand(cards)
"Du fick ett par med valören: 5"
```
1. Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
```text
Exempel på ett kort: ["hjärter", 12]
```

2. Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

3. Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.

Fortsätt att lägga till fler kontroller till funktionen.
```text
Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
pretty_print_card(["hjärter", 5]) → "hjärter fem"
```

Lista med pokerhänder.
 - Ett par (två lika kort)
 - Två par
 - Tretal (tre lika)
 - Straight (5 kort i följd, t.ex. 7-8-9-10-11)
 - Flush / färg (alla kort har samma färg)
 - Hus (par och tretal med olika valörer)
 - Fyrtal
 - Straight flush (5 kort i följd, med samma färg)
 - Femtal

----

## Turtle graphics
Python har ett paket med inbyggda, enkla funktioner för grafik: turtle. Tänk dig att du har en robotarm som håller en penna mot ett papper. Man kan ge olika instruktioner till roboten, för att styra den. Några exempel:

- forward - gå rakt framåt i standardriktningen (peka ursprungligen åt höger)
- backward - gå bakåt
- left, right - sväng vänster eller höger ett antal grader, 360 grader för ett helt varv
- dot - sätt ut en prick med en viss storlek
- speed - normal=6, fast=10, maximal=0

Läs mer här: [Turtle graphics — Python 3.13.1 documentation ](https://docs.python.org/3/library/turtle.html)
Kodexempel:
```python
import turtle as t

# Upprepa 3 gånger
for x in range(3):
    t.forward(100)
    t.left(120)

# Lyft pennan för att flytta utan att rita
t.penup()
t.forward(200)
t.pendown()
t.dot(10, "red")
t.color("blue"
t.forward(50)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
```
1. Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.
2. Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita. Tanken är att du ska kunna kombinera den med kvadratfunktionen, för att rita flera kvadrater. Exempe
```python
for x in range(5):
    t.square()
    t.move_next()
```
3. Bygg om koden så att den ingår i
```python
Tips 1: vad händer om man varierar värdet på range? 
Tips 2: 360 grader motsvarar ett helt varv.
for x in range(7):
    t.forward(40)
    t.right(30)
```
4. Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen. Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.

Bonusuppgift, lär dig rekursiva funktioner med turtle graphics:
[Python Turtle Meets Fractal Art: A Recursive Journey ](https://www.turingtaco.com/python-turtle-meets-fractal-art-a-recursive-journey/)
-----