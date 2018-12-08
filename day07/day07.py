import pandas as pd
import numpy as np

path = 'day07_input.txt'
instructions = pd.read_csv(path, names=['instructions'])
instructions.head()

dep_regex = r'^Step (?P<dependence>\w)'
step_regex = r'step (?P<step>\w)'
instructions['dep'] = instructions['instructions'].str.extract(dep_regex)
instructions['step'] = instructions['instructions'].str.extract(step_regex)

def make_all_letters(instructions):
    deps = instructions['dep'].unique()
    steps = instructions['step'].unique()
    # Get all unique letters in order
    all_letters = sorted(set(np.append(deps, steps)))
    return all_letters

def make_sparse_inst(instructions):
    all_letters = make_all_letters(instructions)
    sparse_inst = pd.DataFrame(data=0, index=all_letters, columns=all_letters)
    sparse_inst['done'] = False

    for index, row in instructions[['step', 'dep']].iterrows():
        step = row['step']
        dep = row['dep']
        sparse_inst.loc[step, dep] = 1

    return sparse_inst

all_letters = make_all_letters(instructions)
sparse_inst = make_sparse_inst(instructions)
sequence = []

prereqs = sparse_inst[all_letters].sum(axis=1)

while not sparse_inst['done'].all():
    # Grab the first alphabetical step with no prerequisites
    ready = sparse_inst[(prereqs == 0) & (sparse_inst['done'] == 0)].index[0]
    # Set the done variable
    sparse_inst['done'].loc[ready] = 1
    sequence.append(ready)
    # Zero out the prerequisites for the completed step
    sparse_inst.loc[:, ready] = 0
    prereqs = sparse_inst[all_letters].sum(axis=1)

part1 = ''.join(sequence)

print(f'Part 1: {part1}')

# Part 2:
available_workers = 5
base_time = 61
elapsed_time = 0
working = []

class Worker(object):
    def __init__(self, job, table):
        self.job = job
        self.table = table
        self.done = False

    def work(self):
        self.table.loc[self.job, 'dur'] -= 1
        job_duration = self.table.loc[self.job, 'dur']
        if job_duration == 0:
            self.done = True 
        

sparse_inst = make_sparse_inst(instructions)
sparse_inst['dur'] = range(base_time, base_time + len(sparse_inst.index))
sparse_inst['in_progress'] = False
prereqs = sparse_inst[all_letters].sum(axis=1)

while not sparse_inst['done'].all():

    # Select new ready steps
    ready = sparse_inst[(prereqs == 0) & 
                        (sparse_inst['done'] == False) &
                        (sparse_inst['in_progress'] == False)].index

    # For each step add a worker if one is available
    for step in ready:
        if available_workers == 0:
            break

        working.append(Worker(step, sparse_inst))
        sparse_inst.loc[step, 'in_progress'] = True
        available_workers -= 1

    # Have each worker work on their task
    for worker in working:
        worker.work()

    # Remove workers that have completed their task
    for worker in working:
        if worker.done:
            working.remove(worker)
            available_workers += 1

    elapsed_time += 1

    # Set step to done
    sparse_inst['done'] = sparse_inst['dur'] == 0
    done = sparse_inst[sparse_inst['dur'] == 0].index
    sparse_inst.loc[:, done] = 0
    prereqs = sparse_inst[all_letters].sum(axis=1)

print(f'Part 2: {elapsed_time}')