n = int(input())
a = list(map(int, input().split()))

p = [0] * (n + 1)
d = {0: [0], 1: [], 2: []}
for i in range(1, n + 1):
    p[i] = (p[i - 1] - a[i - 1]) % 3
    if p[i] == 0:
        d[0].append(i)
    elif p[i] == 1:
        d[1].append(i)
    else:
        d[2].append(i)

jbest = 0
ibest = 0

if len(d[0]) > 1:
    if jbest - ibest < d[0][-1] - d[0][0]:
        jbest = d[0][-1]
        ibest = d[0][0]

if len(d[1]) > 1:
    if jbest - ibest < d[1][-1] - d[1][0]:
        jbest = d[1][-1]
        ibest = d[1][0]
    elif jbest - ibest == d[1][-1] - d[1][0] and d[1][0] < ibest:
        jbest = d[1][-1]
        ibest = d[1][0]

if len(d[2]) > 0:
    if jbest - ibest < d[2][-1] - d[2][0]:
        jbest = d[2][-1]
        ibest = d[2][0]
    elif jbest - ibest == d[2][-1] - d[2][0] and d[2][0] < ibest:
        jbest = d[2][-1]
        ibest = d[2][0]

if (p[ibest] - p[jbest]) == 0 and jbest != 0:
    print(ibest + 1, jbest)
else:
    print(-1)
