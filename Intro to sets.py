def average(array):
    # your code goes here
    average_heights = 0
    for i in set(array):
        average_heights += i

    return average_heights/len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)