from itertools import groupby

for key, group in groupby(input()):
    print(list(group))
    print('({}, {})'.format(len(list(group)), key), end=" ")
