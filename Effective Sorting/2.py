def solution():
    n = int(input())
    limit = [0] + list(map(int, input().split()))
    k = int(input())
    press = list(map(int, input().split()))
    cnt = [0] * (n+1)
    for i in press:
        cnt[i] += 1
    for i in range(1, n+1):
        if cnt[i] > limit[i]:
            print('yes')
        else:
            print('no')


solution()