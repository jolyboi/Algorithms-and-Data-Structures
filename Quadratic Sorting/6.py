n, k = map(int, input().split())

def solution(n, k):
    d = [i for i in range(n, 0, -1)]
    count = 0
    while n > 0 and count != k:
        for i in range(n-1):
            if count != k:
                if d[i] > d[i+1]:
                    d[i], d[i+1] = d[i+1], d[i]
                    count += 1
            else:
                d.reverse()
                for j in d:
                    print(j, end=' ')
                return None
        n -= 1

    d.reverse()
    for j in d:
        print(j, end=' ')


solution(n, k)