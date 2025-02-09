import src.autocomplete_list as kanya

# Krav:
#
# Funktionen autocomplete_list(input, master_list) ska returnera en lista med förslag från master_list som matchar det användaren skriver (input).
# Matchningen ska vara case-insensitive (oberoende av små/stora bokstäver).
# Om input är tom, ska en tom lista returneras.
# Om master_list är tom, ska en tom lista returneras.
# Om inga matchningar hittas, ska en tom lista returneras.

# Acceptanskriterier (AK):
#
# AK1: Om input är tom, returnera en tom lista.
# AK2: Om master_list är tom, returnera en tom lista.
# AK3: Om input matchar början av ett eller flera element i master_list, returnera dessa element.
# AK4: Matchningen ska ignorera små/stora bokstäver (t.ex. "a" ska matcha "Apple").
# AK5: Om input inte matchar något i master_list, returnera en tom lista.

master_list = ["Fisk", "Banan", "Papaya", "Pokpok", "Apple", "Thai mat", "Meatbollar"]


def test_autocomplete_list():
    assert kanya.autocomplete_list("F", master_list) == ["Fisk"]


def test_autocomplete_list():
    assert kanya.autocomplete_list("P", master_list) == ["Papaya", "Pokpok"]


def test_autocomplete_list():
    assert kanya.autocomplete_list("Thai", master_list) == ["Thai mat"]


def test_autocomplete_list():
    assert kanya.autocomplete_list("", master_list) == []


def test_autocomplete_list():
    assert kanya.autocomplete_list(123, master_list) == TypeError


empty_list = []


def test_autocomplete_list():
    assert kanya.autocomplete_list("F", empty_list) == []
