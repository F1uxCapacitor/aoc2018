import re

extract_data = re.compile('^(#)(?P<claim>\d{1,})( @ )(?P<x_coord>\d{1,})(,)'
                          '(?P<y_coord>\d{1,})(: )(?P<x_len>\d{1,})(x)(?P<y_len>\d{1,3}$)')

with open('day3.input', mode='r') as fp:

    for line in fp:

        line = line.strip()

        match = extract_data.match(line)

        data = match.groupdict()

        print(line, data)
