n = int(input())
arr = list(map(int, input().split()))

m_set = set(arr)

print(int(((sum(m_set)*n)-sum(arr))/(n-1)))
