import pandas as pd

df = pd.read_csv('day1.input', header=None, usecols=[0])

frequency_sum = df[0].sum()

print(frequency_sum)