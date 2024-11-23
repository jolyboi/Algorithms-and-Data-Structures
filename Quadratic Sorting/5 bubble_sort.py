n = int(input())
d = list(map(int, input().split()))


def bubble_sort(n):
    unordered = True
    count = 0
    while unordered and n > 0:
        unordered = False
        for i in range(n-1):
            if d[i] > d[i+1]:
                d[i], d[i+1] = d[i+1], d[i]
                count += 1
                unordered = True
        n -= 1

    return count


print(bubble_sort(n))