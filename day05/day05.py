import pandas as pd
path = 'day05_input.txt'


def react(polymer):
    polymer = list(polymer)
    input_polymer = None

    while polymer != input_polymer:
        input_polymer = polymer.copy()
        for index, monomer in enumerate(polymer):
            try:
                next_monomer = polymer[index + 1]
                same_letter = monomer.lower() == next_monomer.lower()
                different = monomer != next_monomer
                if same_letter and different:
                    del polymer[index: index+2]
            except IndexError:
                next

    return ''.join(polymer)


def remove_letter(polymer, letter):
    polymer = list(polymer)

    output_polymer = [monomer if monomer.lower() != letter
                      else ''
                      for monomer in polymer]

    return ''.join(output_polymer)


if __name__ == "__main__":
    with open(path) as file:
        polymer = file.readline()
        length = len(react(polymer))
        print(f'Part 1: {length}')

        letters = set(list(polymer.lower()))
        part2 = pd.DataFrame()
        for letter in letters:
            letter_length = len(react(remove_letter(polymer, letter)))
            part2 = part2.append(pd.DataFrame(
                {'letter': [letter], 'length': [letter_length]}))

        part2 = part2.sort_values(by='length')
        print(f'Part 2: \n {part2}')
