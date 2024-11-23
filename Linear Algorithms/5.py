n, m = map(int, input().split())
h = list(map(int, input().split()))

travel = [0] * (n - 1)
p = [0] * (n)

for i in range(n - 1):
    if h[i] < h[i + 1]:
        travel[i] = 1

for i in range(1, n):
    p[i] = p[i - 1] + travel[i - 1]

for line in range(m):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(p[r] - p[l])

