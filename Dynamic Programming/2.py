n = int(input())
l = list(map(int, input().split()))
l = [0] + l           # O(n)
d = {0: 0, 1: l[1]}

def f(n, l):
    if n in d:
        return d[n]
    else:
        for i in range(2, n+1):
            d[i] = max(f(i-1, l) + l[i], f(i-2, l) + l[i])
    return d[i]

print(f(n, l))