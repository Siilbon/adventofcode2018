class Node():
    total = 0

    def __init__(self, data):
        self.data = data
        self.n_children = int(self.data.pop(0))
        self.n_metadata = int(self.data.pop(0))

    def meta_data(self):
        subtotal = 0
        for meta_data in range(self.n_metadata):
            subtotal += self.data.pop(0)
        return subtotal

    def make_children(self):
        if self.n_children == 0:
            Node.total += self.meta_data()
        else:
            for child in range(self.n_children):
                Node(self.data).make_children()
            self.n_children = 0
            self.make_children()


path = 'day08_input.txt'

with open(path) as file:
    data = file.readline()
    data = [int(x) for x in data.split()]

x = Node(data=data)
x.make_children()
part1 = Node.total
print(f'Part 1: {part1}')

