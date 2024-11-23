n, k = map(int, input().split())
d = list(map(int, input().split()))

i = 0
j = 0
ibest = 0
jbest = n-1
unique_count = 0
seen = {}
go = True

while go:

    if d[j] in seen:
        seen[d[j]] += 1
    else:
        seen[d[j]] = 1

    if seen[d[j]] == 1:
        unique_count += 1

    while unique_count == k:

        if j - i < jbest - ibest:
            ibest, jbest = i, j

        seen[d[i]] -= 1

        if seen[d[i]] == 0:
            unique_count -= 1

        i += 1

    if j < n-1:
        j += 1
    else:
        go = False

print(ibest + 1, jbest + 1)

