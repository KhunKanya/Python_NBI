import src.sordted_number as m


def test_empty_list():
    assert m.is_sorted_ascending([]) is None


def test_single_element_list():
    assert m.is_sorted_ascending(42) == TypeError


def test_sorted_ascending():
    assert m.is_sorted_ascending([1, 2, 3, 4, 5]) == True


def test_not_sorted_ascending():
    assert m.is_sorted_ascending([5, 3, 1, 4, 2]) == False


def test_sorted_ascending_with_duplicates():
    assert m.is_sorted_ascending([1, 2, 2, 3, 4]) == True


def test_not_sorted_ascending_with_duplicates():
    assert m.is_sorted_ascending([1, 2, 2, 3, 2]) == False


def test_sorted_ascending_negative_numbers():
    assert m.is_sorted_ascending([-5, -3, 0, 2, 4]) == True


def test_not_sorted_ascending_negative_numbers():
    assert m.is_sorted_ascending([-3, -5, 0, 2, 4]) == False
