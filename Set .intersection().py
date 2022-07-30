n = int(input())
s_english = set(map(int, input().split()))

b = int(input())
s_french = set(map(int, input().split()))


print(len(s_english.intersection(s_french)))
