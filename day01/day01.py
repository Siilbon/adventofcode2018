def read(path):
    with open(path) as file:
        numbers = [int(x) for x in file.readlines()]
    return numbers

def recalibrate(input_list):
    return sum(input_list)

def loop(input_list):
    ans = []
    total = 0
    while total not in ans:
        for value in input_list:
            ans.append(total)
            total += value
            if total in ans:
                return total
    

if __name__ == "__main__":    
    print('Part1: ', recalibrate(read('day01_input.txt')))
    print('Part2: ', loop(read('day01_input.txt')))