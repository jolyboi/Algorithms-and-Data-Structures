n, x = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ibest = 0
jbest = 1
imin = 0

for j in range(2, n):
    if a[j - 1] < a[imin]:
        imin = j - 1
    if x // a[ibest] * b[jbest] + x % a[ibest] < x // a[imin] * b[j] + x % a[imin]:
        ibest = imin
        jbest = j
if n != 1:
    if x // a[ibest] * b[jbest] + x % a[ibest] <= x:
        print(x)
        print(-1, -1)
    else:
        print(x // a[ibest] * b[jbest] + x % a[ibest])
        print(ibest + 1, jbest + 1)
else:
    print(x)
    print(-1, -1)


