from itertools import combinations

letters_len = int(input())

word = input().split()

tuple_len = int(input())

possible_ways = list(combinations(''.join(sorted(word)), tuple_len))


f = filter(lambda c: "a" in c, possible_ways)
print("{0:.3}".format(len(list(f))/len(possible_ways)))
