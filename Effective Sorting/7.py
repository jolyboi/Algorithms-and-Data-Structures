def f():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort(key=sum_digits, reverse=True)
    return ' '.join(map(str, d))

def sum_digits(a):
    count = 0
    for i in str(a):
        count += int(i)
    return count


print(f())

