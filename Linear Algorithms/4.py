n, k, m = map(int, input().split())
a = list(map(int, input().split()))
res = 0
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = p[i - 1] + a[i - 1]

if p[k + 1] != m:
    for i in range(1, n + 1 - k):
        if p[i + k] - p[i - 1] == m:
            res = i
            break
else:
    res = 1

print(res)