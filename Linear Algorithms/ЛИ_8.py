n, r = map(int, input().split())
d = list(map(int, input().split()))

i = 0
j = 0
count = 0
s = d[j] - d[i]
go = True

while go:
    s = d[j] - d[i]
    if s <= r:
        if j == n - 1:
            go = False
        else:
            j += 1
    else:
        count += (n - j)
        i += 1

print(count)



