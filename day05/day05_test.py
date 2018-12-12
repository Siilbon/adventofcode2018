from day05 import *


def test_react():
    assert react('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'


def test_remove_letter():
    test_word = 'dabAcCaCBAcCcaDA'
    assert remove_letter(test_word, 'a') == 'dbcCCBcCcD'
    assert remove_letter(test_word, 'c') == 'dabAaBAaDA'
    assert len(react(remove_letter(test_word, 'a'))) == 6
    assert len(react(remove_letter(test_word, 'b'))) == 8
    assert len(react(remove_letter(test_word, 'c'))) == 4
    assert len(react(remove_letter(test_word, 'd'))) == 6
