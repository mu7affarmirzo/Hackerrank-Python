n = int(input())
s = set(map(int, input().split()))

o = int(input())

for i in range(o):
    operation = input().split()
    if operation[0] == "pop":
        s.pop()
    elif operation[0] == "remove":
        _ = int(operation[1])
        s.remove(_)
    elif operation[0] == "discard":
        _ = int(operation[1])
        s.discard(_)

print(sum(s))
