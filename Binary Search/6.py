n, m = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))


def left_right(i):
    l = -1
    r = n
    while r - l > 1:
        m = (r + l) // 2
        if a[m] < i:
            l = m
        else:
            r = m
    left = r + 1
    l = -1
    r = n
    while r - l > 1:
        m = (r + l) // 2
        if a[m] <= i:
            l = m
        else:
            r = m
    right = l + 1
    if right - left >= 0:
        return left, right
    return 0


def main():
    for i in b:
        ans = left_right(i)
        if type(ans) == tuple:
            print(ans[0], end=' ')
            print(ans[1])
        else:
            print(ans)


main()