from math import floor

#2 Skriv färdigt testfallen test_empty_list och test_number_list.
def sum_list(list):
    return sum(list)

#3a
# Function that take one string, and count how many vowels are inside
# Start the counter at 0, and increase by 1 for each vowel.
def count_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
    total = 0
    # Below. Loop through every word in the letter, and checking that word in the above list
    for letter in str(word):
        if letter in vowels:
            total = total + 1
    return total


# 4.
def find_max(list):
    if len(list) == 0:
        return None
    if not all(isinstance(item, (int, float)) for item in list):
        return ValueError

    largest_num = list[0]
    for item in list:
        if item > largest_num:
            largest_num = item
    return largest_num


# 5.
def find_2nd_max(list):
    if len(list) == 0:
        return None
    if not all(isinstance(item, (int, float)) for item in list):
        return ValueError
    sorted_list = sorted(list, reverse=True)
    if len(list) == 1:
        return None
    if sorted_list[0] == sorted_list[1]:
        return sorted_list[0]
    else:
        return sorted_list[1]


##### 2
# 1
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32


# 2
def count_words(string):
    if not isinstance(string, str):
        return ValueError
    if len(string) < 1:
        return None

    returnval = 0

    for word in string.split(" "):
        if word.isalnum():
          returnval = returnval + 1

    return returnval

# 3
def find_median(list):
    if len(list) == 0:
        return None
    if not all(isinstance(item, (int, float)) for item in list):
        return ValueError
    list.sort()
    # Om det ar jamnt eller udda antal element i listan
    if len(list) == 2:
        return list[0] / list[1]
    elif len(list) == 1:
        return list[0]
    if len(list) % 2 == 0: # is even
        middle_bot = int((len(list) / 2) - 1)
        middle_top = int(len(list) / 2)
        return (list[middle_top] + list[middle_bot]) / 2
    else:
        return list[floor(len(list)/2)]









