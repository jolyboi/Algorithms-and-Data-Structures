n = int(input())
a = list(map(int, input().split(" ")))

ibest = 0
jbest = 1
imin = 0

for j in range(2, n):
    if a[j - 1] < a[imin]:
        imin = j - 1
    if a[j] / a[imin] >= a[jbest] / a[ibest]:
        jbest = j
        ibest = imin

if a[jbest] / a[ibest] <= 1:
    print(0, 0)
else:
    print(ibest + 1, jbest + 1)