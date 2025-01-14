# Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.

system = input("Celcius (c) eller fahrenheit(f)?: ")
grader = float(input("Skriv in en temperatur: "))

if system == "f":
    c = (grader - 32) / 1.8
    print(f"{grader}°F är {c} grader celcius")
    if c < 10:
        print("Det är kallt, ta på dig vinterkläder!")
    elif c >= 20:
        print("Det är varmt, packa badkläder!")
elif system == "c":
    f = 1.8 * grader + 32
    print(f"{grader}°C är {f} grader fahranheit")
    if grader < 10:
        print("Det är kallt, ta på dig vinterkläder!")
    elif grader >= 20:
        print("Det är varmt, packa badkläder!")
else:
    print("Felaktigt system. Enbart '°C' och °F är godkänt.")
