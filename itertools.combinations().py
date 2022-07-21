from itertools import combinations

word, length = input().split()

for j in range(1, int(length) + 1):
    possible_ways = list(combinations(''.join(sorted(word)), int(j)))

    for i in possible_ways:
        print(''.join(i))
