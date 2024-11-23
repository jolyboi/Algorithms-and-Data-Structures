n, k = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

def find_closest(x):
    l = -1
    r = n
    while r - l > 1:
        m = (r+l) // 2
        if l1[m] == x:
            return l1[m]
        elif l1[m] < x:
            l = m
        else:
            r = m
    if l == -1:
        return l1[r]
    if r == n:
        return l1[l]
    if abs(x-l1[l]) < abs(x-l1[r]):
        return l1[l]
    if abs(x-l1[l]) > abs(x-l1[r]):
        return l1[r]
    else:
        ans = min(l, r)
        return l1[ans]


def main():
    for i in l2:
        print(find_closest(i))


main()