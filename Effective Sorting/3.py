def solution():
    l, n, m = map(int, input().split())
    beg = [0] * (l+1)
    end = [0] * (l+1)
    sum_beg = [0] * (l+1)
    sum_end = [0] * (l+1)
    # counting beginnings and ends for socks
    for i in range(n):
        b, e = map(int, input().split())
        beg[b] += 1
        end[e] += 1
    # the prefix sum for beginning
    sum_beg[1] = sum(beg)
    for i in range(2, l+1):
        sum_beg[i] = sum_beg[i-1] - beg[i-1]
    # the prefix sum for end
    sum_end[1] = sum(end)
    for i in range(2, l+1):
        sum_end[i] = sum_end[i-1] - end[i-1]
    # calculating the sum
    for i in range(m):
        point = int(input())
        if point != l:
            ans = sum_end[point] - sum_beg[point+1]
        else:
            ans = sum_end[point]
        print(ans)


solution()


