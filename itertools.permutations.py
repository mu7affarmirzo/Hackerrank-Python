from itertools import permutations

word, length = input().split()

possible_ways = list(permutations(''.join(sorted(word)), int(length)))

for i in possible_ways:
    print(''.join(i))
    