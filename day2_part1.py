from collections import Counter
from functools import partial
import pandas as pd


def num_chars_in_seq(seq, num):

    counter = Counter(seq)

    unique_character_counts = set(counter.values())

    if num in unique_character_counts:

        return True

    else:

        return False


has_two = partial(num_chars_in_seq, num=2)

has_three = partial(num_chars_in_seq, num=3)

data = pd.read_csv('day2.input', header=None, names=['container_id'])

data['has_two'] = data['container_id'].apply(has_two)

data['has_three'] = data['container_id'].apply(has_three)

twos = data[data['has_two'] == True]['has_two'].size

threes = data[data['has_three'] == True]['has_three'].size

print(twos * threes)
