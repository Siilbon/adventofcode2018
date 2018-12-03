from day02 import *

def test_get_freq():
    assert get_freq('abcdef') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
    assert get_freq('bababc') == {'a': 2, 'b': 3, 'c': 1}
    assert get_freq('abbcde') == {'a': 1, 'b': 2, 'c': 1, 'd': 1, 'e': 1}
    assert get_freq('abcccd') == {'a': 1, 'b': 1, 'c': 3, 'd': 1}
    assert get_freq('aabcdd') == {'a': 2, 'b': 1, 'c': 1, 'd': 2}
    assert get_freq('abcdee') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 2}
    assert get_freq('ababab') == {'a': 3, 'b': 3}

def test_reoccuring():
    assert reoccuring('abcdef', 2) == False
    assert reoccuring('bababc', 2) == True
    assert reoccuring('abbcde', 2) == True
    assert reoccuring('abcccd', 2) == False
    assert reoccuring('aabcdd', 2) == True
    assert reoccuring('abcdee', 2) == True
    assert reoccuring('ababab', 2) == False

    assert reoccuring('abcdef', 3) == False
    assert reoccuring('bababc', 3) == True
    assert reoccuring('abbcde', 3) == False
    assert reoccuring('abcccd', 3) == True
    assert reoccuring('aabcdd', 3) == False
    assert reoccuring('abcdee', 3) == False
    assert reoccuring('ababab', 3) == True

def test_checksum():
    assert checksum('day02_input_test.txt') == 12