from day01 import recalibrate, loop

def test_recalibrate():
    assert recalibrate([1, 1, 1]) == 3
    assert recalibrate([1, 1, -2]) == 0
    assert recalibrate([-1, -2, -3]) == -6

def test_loop():
    assert loop([1, -1]) == 0
    assert loop([3, 3, 4 , -2, -4]) == 10
    assert loop([-6, 3, 8, 5, -6]) == 5
    assert loop([7, 7, -2, -7, -4]) == 14