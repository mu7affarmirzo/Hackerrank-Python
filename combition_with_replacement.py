from itertools import combinations_with_replacement

word, length = input().split()

possible_ways = list(combinations_with_replacement(''.join(sorted(word)), int(length)))

for i in possible_ways:
    print(''.join(i))

