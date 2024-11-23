# n = int(input())
# d = {0:0, 1:1, 2:2, 3:4}
# def f(n):
#     if n in d:
#         return d[n]
#     else:
#         ans = f(n-1) + f(n-2) + f(n-3)
#         d[n] = ans
#         return ans
#
# print(f(n))



n = int(input())
d = {0:0, 1:1, 2:2, 3:4}
def f(n):
    if n in d:
        return d[n]
    else:
        for i in range(4, n + 1):
            d[i] = f(i-1) + f(i-2) + f(i-3)
    return d[i]
print(f(n))

# 1132436852
