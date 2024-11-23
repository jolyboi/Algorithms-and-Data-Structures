n = int(input())
d = []
for i in range(n):
    d.append(list(map(int, input().split())))
    j = i - 1
    tmp = d[i]
    while j >= 0 and ((d[j][1] < tmp[1]) or (d[j][1] == tmp[1] and d[j][0] > tmp[0])):
        d[j+1] = d[j]
        j -= 1
    d[j+1] = tmp


for i in d:
    print(f'{i[0]} {i[1]}')
