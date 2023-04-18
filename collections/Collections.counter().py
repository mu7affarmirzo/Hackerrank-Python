from collections import Counter

number_of_shoes = int(input())

all_shoes = Counter(map(int, input().split()))

customers = int(input())

total_purchase = 0

print(f"shoes: {all_shoes}")
for i in range(customers):
    size, x_i = map(int, input().split())

    if not all_shoes[size] == 0:
        print(f"shoes in the store: {all_shoes[size]}. Size: {size}")
        total_purchase += x_i
        all_shoes[size] -= 1

print(total_purchase)