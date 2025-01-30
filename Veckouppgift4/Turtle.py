import turtle as t

t.setup(1820, 1000)

def draw_square(side_length):
    for _ in range(4):            # Upprepa 4 gånger för att rita 4 sidor
        t.forward(side_length)    # gå framåt enligt det värde som anges i (side_length).
        t.left(90)

def move_next(distance):
    t.penup()
    t.forward(distance)
    t.pendown()
for _ in range(5):
    draw_square(100)
    move_next(110)

t.speed(10)

#3. Rita en komplett cirkel med parametrar
def draw_circle(steps, step_length, angle):
    for _ in range(steps):
        t.forward(step_length)
        t.right(angle)

draw_circle(36, 20, 10)  # användning
t.mainloop()