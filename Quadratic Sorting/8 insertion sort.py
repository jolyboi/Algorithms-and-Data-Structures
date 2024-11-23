n = int(input())
d = list(map(int, input().split()))

def insertion_sort(n):
    for i in range(1, n):
        changed = False
        tmp = d[i]
        j = i - 1
        while j >= 0 and d[j] > tmp:
            changed = True
            d[j+1] = d[j]
            j -= 1
        d[j+1] = tmp
        if changed:
            for a in range(len(d)):
                if a == len(d) - 1:
                    print(d[a])
                else:
                    print(d[a], end=' ')



insertion_sort(n)