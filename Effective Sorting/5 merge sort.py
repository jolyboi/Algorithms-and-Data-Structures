def merge(a, b):
    length1 = len(a)
    length2 = len(b)
    i = 0
    j = 0
    while i < length1 and j < length2:
        if a[i] <= b[j]:
            a.append(a[i])
            i += 1
        else:
            a.append(b[j])
            j += 1
    a.extend(a[i:length1])
    a.extend(b[j:])
    return a[length1:]


def msort(a):
    if len(a) == 1:
        return a
    k = len(a) // 2
    return merge(msort(a[:k]), msort(a[k:]))


def main():
    n = int(input())
    d = list(map(int, input().split()))
    res = msort(d)
    return ' '.join(map(str, res))


print(main())