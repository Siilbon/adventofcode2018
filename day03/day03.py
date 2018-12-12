import numpy as np
import pandas as pd

path = 'day03_input.txt'
orders = pd.read_csv(path, names=['orders'],
                     index_col=False,
                     delimiter='\n')


order_pattern = r'#(?P<order_num>\d+)\s@\s(?P<x1>\d+),(?P<y1>\d+):\s(?P<width>\d+)x(?P<height>\d+)'

orders = orders['orders'].str.extract(pat=order_pattern,
                                      expand=True)

orders = orders.applymap(pd.to_numeric)
orders['x2'] = orders['x1'] + orders['width']
orders['y2'] = orders['y1'] + orders['height']


def make_fabric(orders_df):
    array_max_cols = max(orders_df['x2'])
    array_max_rows = max(orders_df['y2'])
    fabric = np.zeros((array_max_rows, array_max_cols))
    return fabric


def reserve_fabric(fabric, order):
    fabric_rows_min = order['y1']
    fabric_rows_max = order['y2']
    fabric_cols_min = order['x1']
    fabric_cols_max = order['x2']
    fabric[fabric_rows_min: fabric_rows_max,
           fabric_cols_min: fabric_cols_max] += 1


def count_overlaps(orders_df):
    fabric = make_fabric(orders_df)
    orders_df.apply(lambda row: reserve_fabric(
        fabric=fabric, order=row), axis=1)
    overlaps = np.where(fabric > 1, 1, 0).sum()
    return overlaps


def check_order(fabric, order):
    fabric_rows_min = order['y1']
    fabric_rows_max = order['y2']
    fabric_cols_min = order['x1']
    fabric_cols_max = order['x2']
    ordered_section = fabric[fabric_rows_min: fabric_rows_max,
                             fabric_cols_min: fabric_cols_max]
    if np.where(ordered_section == 1, 0, 1).sum() == 0:
        return order['order_num']
    else:
        return None


def orders_with_no_overlaps(orders_df):
    fabric = make_fabric(orders_df)
    orders_df.apply(lambda row: reserve_fabric(
        fabric=fabric, order=row), axis=1)
    ans = orders_df.apply(lambda row: check_order(
        fabric=fabric, order=row), axis=1)
    ans = int(ans[ans.notna()].item())
    return ans


print(f'Part1: {count_overlaps(orders)}')
print(f'Part2: {orders_with_no_overlaps(orders)}')
