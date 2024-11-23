def f():
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    res = set()
    for i in a|b:
        if i in a and i in b:
            continue
        else:
            res.add(i)
    print(len(res))
    res_sorted = sorted(list(res))
    print(' '.join(map(str, res_sorted)))


f()