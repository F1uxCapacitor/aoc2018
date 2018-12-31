import pandas as pd

df = pd.read_csv('day1.input', header=None, usecols=[0])

frequency = 0

freqs = set()

freqs.add(frequency)

cont = True

while cont is True:

    for _, i in df[0].iteritems():

        frequency += i

        if frequency in freqs:

            print(frequency)

            cont = False

            break

        else:

            freqs.add(frequency)
