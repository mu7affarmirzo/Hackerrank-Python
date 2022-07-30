a = int(input())

set_1 = set(map(int, input().split()))

b = int(input())

set_2 = set(map(int, input().split()))

l = sorted((set_1.difference(set_2)).union(set_2.difference(set_1)))

print("\n".join([str(element) for element in l]))

