countries_n = int(input())

countries_set = set()
for i in range(countries_n):
    countries_set.add(input())

print(len(countries_set))