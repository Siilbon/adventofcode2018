def read(path):
    with open(path) as file:
        ids = file.readlines()
    return ids

def get_freq(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    
    return freq

def reoccuring(word, number):
    return number in get_freq(word).values()

def checksum(path):
    ids = read(path)
    twos, threes = 0, 0
    for id in ids:
        twos += reoccuring(id, 2)
        threes += reoccuring(id, 3)

    return twos*threes

def compare(name1, name2):
    num_diff = 0
    index_diff = 0
    for index, letter1, letter2 in zip(range(len(name1)), name1, name2):
        if letter1 != letter2:
            num_diff += 1
            index_diff = index
        if num_diff > 1:
            return False

    return name1[:index_diff] + name1[index_diff+1:]

def compare_all(path):
    ids = read(path)
    for id in ids:
        for id2 in ids:
            if id == id2:
                pass
            elif compare(id, id2) != False:
                return compare(id, id2)

    

    


if __name__ == "__main__":
    print('Part 1: ', checksum('day02_input.txt'))
    print('Part 2: ', compare_all('day02_input.txt'))