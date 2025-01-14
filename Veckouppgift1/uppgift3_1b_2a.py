#1a, 1b
tal1 = int(input("skriv ett heltal: "))
tal2 = int(input("skriv ett heltal: "))
print(tal1 + tal2)
#2a, 2b
pris = 2000
rea_procent = float(input('Ange rabatt procent: '))
slut_pris = (pris * rea_procent) / 100
betala = pris - slut_pris
print(f"Rabatten med {rea_procent}% blir {slut_pris}kr. Slutpriset blir då {betala}kr.")
