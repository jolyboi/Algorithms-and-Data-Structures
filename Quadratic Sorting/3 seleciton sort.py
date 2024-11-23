n, k = map(int, input().split())
d = list(map(int, input().split()))


def solution(n, k, d):
    for i in range(n-1):
        imax = i
        for j in range(i+1, n):
            if d[j] > d[imax]:
                imax = j
        d[i], d[imax] = d[imax], d[i]
        if i == k - 1:
            return d[i]
    return d[k-1]


print(solution(n, k, d))