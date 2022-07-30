n = int(input())
s_english = set(map(int, input().split()))

a = int(input())

for i in range(a):
    inp = list(input().split())
    temp_set = set(map(int, input().split()))
    if inp[0] == 'intersection_update':
        s_english.intersection_update(temp_set)
    elif inp[0] == 'update':
        s_english.update(temp_set)
    elif inp[0] == 'symmetric_difference_update':
        s_english.symmetric_difference_update(temp_set)
    elif inp[0] == 'intersection_update':
        s_english.intersection_update(temp_set)
    elif inp[0] == 'difference_update':
        s_english.difference_update(temp_set)

print(sum(s_english))



