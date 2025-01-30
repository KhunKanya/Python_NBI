#1
def my_function(string):
    print(f"{string} är en riktig hacker")

#2a, 2b
def eko(string, count):
    print(string * count)

#3
def loop(end):
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:
            break
        x = x + 1
    print(y)

#4
def last(lista):
    return lista[-1]

#5
def cut_edges(lista):
    return lista[1:-1]

#6 Lös felen i koden.
def increase(x):
    x += 1     # måste vi flytta x += 1 innan return.
    return x
print(increase(1))

#7
def average(x, y):
    return (x + y) / 2

#8
def pretty_print(lista):
    if not lista:
        print("Listan är tom.")
    else:
        print(f"Listan har {len(lista)} element:")
        for i, item in enumerate(lista):
            print(f"{i + 1}. {item}")