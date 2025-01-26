#4 Figurer med loopar

def print_a():
    for y in range(1, 7):
        s = "#"
        for x in range(1, 9):
            if x == y:
                s += "."
            else:
                s += "."
        print(s)

def print_b():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == y:
                s += "#"
            else:
                s += "."
        print(s)

def print_c():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x in range(3, 6):
                s += "#"
            else:
                s += "."
        print(s)

def print_d():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if y == 3 or x == 3:
                s += "#"
            else:
                s += "."
        print(s)

def print_e():
    z = 6
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == 5 or x == z:
                s += "#"
            else:
                s += "."
        z = z - 1
        print(s)

def print_f():
    z = 6
    x1 = 1
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x == z or x == x1:
                s += "#"
            else:
                s += "."
        z = z - 1
        x1 = x1 + 1
        print(s)

def print_g():
    for y in range(1, 7):
        s = ""
        for x in range(1, 9):
            if x % 2 != 0:
                s += "#"
            else:
                s += "."
        print(s)

print_g()



