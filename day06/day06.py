import pandas as pd
import numpy as np

path = 'day06_input.txt'
nodes = pd.read_csv(path, names=['row', 'col'])

nodes['row'] = nodes['row'] - nodes['row'].min()
nodes['col'] = nodes['col'] - nodes['col'].min()
nodes['count'] = 0
nodes['edge'] = 0

max_dist = 10000
part2 = 0

for row in range(nodes['row'].max() + 1):
    for col in range(nodes['col'].max() + 1):
        # Check for edge
        if (row == 0) | (col == 0) | (row == nodes['row'].max()) | (col == nodes['col'].max()):
            edge = 1
        else:
            edge = 0
        
        # If only 1 closest neighbor add to the count
        nodes['dist'] = abs(nodes['row'] - row) + abs(nodes['col'] - col)    
        number_of_closest_nodes = sum(nodes['dist'] == nodes['dist'].min())
        if number_of_closest_nodes == 1:
            min_node_idx = nodes['dist'].idxmin()
            nodes['count'][min_node_idx] += 1
            nodes['edge'][min_node_idx] += edge

        else:
            pass
        
        if nodes['dist'].sum() < max_dist:
            part2 += 1


part1 = nodes[nodes['edge'] == 0].sort_values(by='count', ascending=False)['count'].head(1).item()

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
