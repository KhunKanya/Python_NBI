def is_sorted_ascending(numbers):
    # Sanity check
    if not isinstance(numbers, list):
        return TypeError
    if not all(isinstance(item, (int, float)) for item in numbers):
        return ValueError
    if len(numbers) == 0:
        return None


    start_index = 0
    for i in numbers:
        if start_index == len(numbers) - 1:
            return True
        if numbers[start_index] <= numbers[start_index + 1]:
            start_index = start_index + 1
            continue
        else:
            return False

# 4a Vilka ekvivalensklasser har numbers?
#, negativa nummer, posititiva nummer, extremt höga/låga nummer, strängar (atoi), tom lista
# undefined list, 1 element bara
# 4b Formulera krav och acceptanskriterier för funktionen.
# 4c Skriv testfall för funktionen.

# Sanity check