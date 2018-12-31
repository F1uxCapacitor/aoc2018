import pandas as pd

data = pd.read_csv('day1.input', header=None, squeeze=True)

frequency = 0

freqs = set()

freqs.add(frequency)

cont = True

while cont is True:

    for _, i in data.iteritems():

        frequency += i

        if frequency in freqs:

            print(frequency)

            cont = False

            break

        else:

            freqs.add(frequency)
