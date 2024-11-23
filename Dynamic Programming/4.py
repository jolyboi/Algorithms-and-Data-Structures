n = int(input())
d = {1: 0, 2: 1, 3: 1}

def f(n):
    if n in d:
        return d[n]
    else:
        for i in range(4, n+1):
            d[i] = f(i-1) + 1
            if i % 2 == 0:
                d[i] = min(d[i], f(i/2) + 1)
            if i % 3 == 0:
                d[i] = min(d[i], f(i/3) + 1)

        return d[n]

print(f(n))