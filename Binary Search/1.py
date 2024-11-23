def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    m = int(input())
    q = list(map(int, input().split()))

    for x in q:
        l = -1
        r = n
        while r - l > 1:
            m = (r+l) // 2
            if a[m] <= x:
                l = m
            else:
                r = m
            # print(l, r)

        print(l+1, end=' ')


main()
