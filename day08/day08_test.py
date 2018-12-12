from day08 import *
path = 'day08_input_test.txt'

with open(path) as file:
    sample = file.readline()

def test_crawler():
    assert crawler(sample) == 138

def test_Node():
    node1 = Node([3, 2])
    assert node1.children == 3
    assert node1.metadata == 2
