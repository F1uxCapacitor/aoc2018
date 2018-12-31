from collections import Counter
from functools import partial
import pandas as pd


def count_vals(sequence, count):

    counter = Counter(sequence)

    unique_counts = set(counter.values())

    if count in unique_counts:

        return True

    else:

        return False


two_count = partial(count_vals, count=2)

three_count = partial(count_vals, count=3)

df = pd.read_csv('day2.input', header=None, usecols=[0])

df['two_count'] = df[0].apply(two_count)

df['three_count'] = df[0].apply(three_count)

twos = df[df['two_count'] == True]

threes = df[df['three_count'] == True]

print(twos.size * threes.size)
