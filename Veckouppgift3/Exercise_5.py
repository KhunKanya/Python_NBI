#5 Gissa talet.    Gör ett spel som slumpar ett hemligt tal mellan 1 och 100.
print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

import random
secret = random.randint(1, 100)
guess_count = 0
print(f"Cheating correct answer for test {secret}")

while True:
    try:
        guess = int(input("vilket det är?"))
    except ValueError:
        print("Nu blev det fel. Skriv en siffra.")
        continue
    guess_count += 1
    if guess < secret:
        print("Nej, det är för lågt!")
        if secret - guess <= 5:
            print("Nu börjar det brännas!")
    elif guess > secret:
        print("Nej, det är för högt!")
        if guess - secret <= 5:
            print("Nu börjar det brännas!")    # version2 skriv ut om man är nära ifall man gissar högst 5 ifrån
    elif guess == secret:
        print(f'Det är rätt!! Du gjorde det på {guess_count} gissningar.')
        break









