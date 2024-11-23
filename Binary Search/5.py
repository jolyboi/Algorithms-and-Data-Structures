def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    for i in b:
        print(check(i, n, a))


def check(num, length, li):
    l = -1
    r = length
    while r - l > 1:
        m = (l+r) // 2
        if li[m] < num:
            l = m
        elif li[m] > num:
            r = m
        else:
            return 'YES'
    return 'NO'


main()
