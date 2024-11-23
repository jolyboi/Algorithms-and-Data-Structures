def merge():
    x = int(input())
    a = [i ** 2 for i in range(1, x + 1)]
    b = [i ** 3 for i in range(1, x + 1)]
    res = []
    i = 0
    j = 0
    count = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        elif a[i] > b[j]:
            res.append(b[j])
            j += 1
        else:
            res.append(a[i])
            i += 1
            j += 1
        count += 1
        if count == x:
            return res[-1]


print(merge())

