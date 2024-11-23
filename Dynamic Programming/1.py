n = int(input())
def f(n, d):
    if n in d:
        return d[n]
    else:
        ans = f(n-1, d) + f(n-2, d)
        d[n] = ans
        return ans
d = {0:0, 1:1}
print(f(n, d))
