import pandas as pd

data = pd.read_csv('day1.input', header=None, squeeze=True)

frequency_sum = data.sum()

print(frequency_sum)
