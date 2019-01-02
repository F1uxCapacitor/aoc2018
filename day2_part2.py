from functools import partial
import pandas as pd

data = pd.read_csv('day2.input', header=None, names=['containerId'])

data.sort_values(by='containerId', inplace=True)

data.reset_index(drop=True, inplace=True)

for row in data.itertuples():

    idx = row.Index

    value = row.containerId

    prev_value = data.iloc[idx - 1, 0]

    grouped = zip(prev_value, value)

    chars = pd.DataFrame(list(grouped), columns=['prev', 'current'])

    chars['equal'] = chars['prev'] == chars['current']

    num_diffs = chars[chars['equal'] == False]['equal'].size

    if num_diffs == 1:

        print(chars[chars['equal'] == True]['prev'].str.cat())
