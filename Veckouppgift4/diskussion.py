#1a
def foo(test):
    print(test)

foo("hej")

#1b
def fun1(x, y):
    return x * y

print(fun1(3, 5))

#1c
def fun1(x, y):
    return x * y
print(fun1(3, 5))

#1d
def fun2(i):
    return 5 * i
x = 2
y = 3
a = fun2(fun2(x) + fun2(y))  # 10 + 15 * 5 = 125
print(a)

#1e
a = 5
def fun3(a):   #anvanda inte fun3
    a += 1

a += 2
print(a)

#1f
def foo(i):
    return 2*i*i

def goo(foobar, y):       # foobar = x
    return foobar(y)      # y = 3

a = goo(foo, 3);          # Beräkna värdet  2 * (3 * 3) = 2 * 9  = 18
print(a)

# 1g Funktionen "isinstance" kan kontrollera en variabels datatyp. Vad gör funktionen is_number? Går det att förbättra koden?
def is_number(x):
    if isinstance(x, int): #(จำนวนเต็ม)
        return True
    elif isinstance(x, float):  #float (จำนวนทศนิยม)
        return True
    return False  #ถ้าไม่ใช่ทั้ง int และ float จะ return False

print(is_number(5.5)) #ส่งค่า 5.5 เข้าไปในฟังก์ชัน ซึ่ง 5.5 เป็นชนิด float ดังนั้นจะได้ผลลัพธ์เป็น True
print(is_number(42))

#1h
def average_words(strings):   #Används för att filtrera ord med en längd på 5-7 tecken.
    found = []
    for item in strings:
        if 4 < len(item) < 8:   #มากกว่า 4 และน้อยกว่า 8
            found.append(item)
    return found

print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))

#### kan använda List Comprehension för att minska antalet rader och göra koden mer kompakt. #######
def average_words(strings):
    return [item for item in strings if 4 < len(item) < 8]

print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))

########_____________________________________________________________________________________________


def find_min(numbers):
    try:
        counter = numbers[0]
    except IndexError:
        print("Empty list, please come again")
        return False
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])
