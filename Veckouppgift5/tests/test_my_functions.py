import src.my_functions as m


# 2 Skriv färdigt testfallen test_empty_list och test_number_list.
def test_empty_list():
    expected = 0
    actual = m.sum_list([])
    assert actual == expected


def test_number_list():
    assert m.sum_list([5]) == 5
    assert m.sum_list([1, 2, 3, 4]) == 10
    assert m.sum_list([5, 6, 7]) == 18
    assert m.sum_list([8, 9, 10]) == 27

#3a
def test_no_vowels():
    assert m.count_vowels("qwrt") == 0
    assert m.count_vowels("Tt") == 0
    assert m.count_vowels("123 123") == 0
    assert m.count_vowels("") == 0
    assert m.count_vowels("fisk") == 1


# 4
def test_find_max():
    assert m.find_max([1, 2, 3, 4]) == 4
    assert m.find_max([7, 1, -54, 100, 23]) == 100
    assert m.find_max([-2, -1, -76]) == -1
    assert m.find_max([0]) == 0
    assert m.find_max([]) == None
    assert m.find_max(['hej', 2, 5]) == ValueError


# 5
def test_find_2nd_max():
    assert m.find_2nd_max([1, 2, 3, 4]) == 3
    assert m.find_2nd_max([7, 1, -54, 100, 23]) == 23
    assert m.find_2nd_max([-2, -1, -76]) == -2
    assert m.find_2nd_max([-2, -76, -1, -1]) == -1
    assert m.find_2nd_max([5]) == None
    assert m.find_2nd_max([]) == None
    assert m.find_2nd_max(['hej', 2, 5]) == ValueError


#### 2
# 1
def test_c_to_f():
    assert m.c_to_f(32) == 89.6
    assert m.c_to_f(-32) == -25.6
    assert m.c_to_f(-300) == None
    assert m.c_to_f(100) == 212


# 2
# Krav:
# Ska returnera antelet ord
# Ord ar separerade med mellanslag
# Inga ord alls ska returnera None

def test_count_words():
    assert m.count_words("") == None
    assert m.count_words("My little Pony") == 3
    assert m.count_words("Fisk") == 1
    assert m.count_words("I love Thai Food") == 4
    assert m.count_words(
        "jfgdfg  hgffg e f fdsfdsf fs fdsfdsf gdgdujhfjdis  ijrifj  ijerfjiogj ij ojergi j jigjireg j ijgiregj ji jiergjiregjoig jh yugjkegnr huire hiergj jjii   ijregijrgijer j iej ioej irejergjier joirkgoerkg ") > 20
    assert m.count_words(12) == ValueError


# 3
# Krav:
# Returnera medianvardet, om antalet element ar jamnt, returnera medeltalet av de tva medianerna.
# Om listan ar tom, rturnera none
# Om listan innehaller strings, returnera ValueError

def test_find_median():
    assert m.find_median([]) == None
    assert m.find_median(["Fisk", "Banan"]) == ValueError
    assert m.find_median([12, "fisk"]) == ValueError
    assert m.find_median([1, 2, 3, 699, 54, 32, 76]) == 32
    assert m.find_median([1, 2, 3, 34, 699, 54, 32, 76]) == 33
    assert m.find_median([-32, -31, 234, 65, 1234, 34]) == 49.5

# 8 / 2 = 3


# 4
