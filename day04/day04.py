import numpy as np
import pandas as pd

# Read in the log file and extract the time and guard numbers
notes = pd.read_csv('day04_input.txt', names=['notes'])
notes = notes['notes'].str.extract(
    pat=r'\[\d{4}-(?P<minutes>.*)\] (?P<text>.*)')
notes['minutes'] = pd.to_datetime(notes['minutes'], format='%m-%d %H:%M')
notes['guard'] = notes['text'].str.extract(pat=r'Guard #(?P<guard>\d+)')
notes.sort_values(by='minutes', inplace=True)
notes.head()

# This table has all the information about sleeping.
non_guards = notes[notes['guard'].isna()].loc[:, ['minutes', 'text']]

# This table has when the guard goes on shift.
guard_watch = notes[notes['guard'].notna()].set_index('minutes')

# The round below is so that each guard effectively starts at midnight
guard_watch.set_index(guard_watch.index.round(freq='H'), inplace=True)
guard_watch = guard_watch.reset_index().loc[:, ['minutes', 'guard']]

# Build a table with 60 mins per day from midnight to 1 am
elf_watch = pd.DataFrame(columns=['minutes'])
for date in pd.date_range(start=notes['minutes'].min().date(), end=notes['minutes'].max().date()):
    elf_watch = pd.concat([elf_watch, pd.DataFrame(pd.date_range(start=date, periods=60, freq='min'), columns=['minutes'])],
                          ignore_index=True)

# Merge the tables and do a forward fill to record the state of each guard
elf_watch = elf_watch.merge(non_guards, left_on='minutes',
                            right_on='minutes', how='outer').sort_values(by='minutes')
elf_watch = elf_watch.merge(guard_watch, left_on='minutes',
                            right_on='minutes', how='outer').sort_values(by='minutes')
elf_watch.set_index('minutes', inplace=True)
elf_watch.sort_index(inplace=True)

elf_watch.fillna(method='ffill', inplace=True)
totals = elf_watch.groupby(['guard', 'text']).size(
).sort_values(ascending=False).reset_index()

part1_elf = totals[totals['text'].str.contains('falls asleep')].head(1)[
    'guard'].item()

elf_watch['min'] = elf_watch.index.time

part1_min = elf_watch[(elf_watch['guard'] == '1987') & (
    elf_watch['text'] == 'falls asleep')]['min'].value_counts().head(1).index

print(f'Part1: Guard #{part1_elf} at min {part1_min}')

sleep = elf_watch[elf_watch['text'] == 'falls asleep']
part2 = sleep.groupby(['guard', 'min']).size().sort_values(
    ascending=False).reset_index().head(1)

print(f'Part2: \n {part2}')
