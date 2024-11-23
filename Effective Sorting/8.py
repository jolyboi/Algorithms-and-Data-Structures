def f():
    n = int(input())
    num = []
    for i in range(n):
        a = str(input())
        num.append(a)
    num.sort(key=lambda x: x*100, reverse=True)
    return ''.join(map(str, num))


print(f())


