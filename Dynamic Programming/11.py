# РЕКУРСИВНОЕ РЕШЕНИЕ ОТ КОНЦА ДО НАЧАЛА
import sys
sys.setrecursionlimit(10 ** 8)

k, p = map(int, input().split())
dp = {1: 0, 2: 1, 3: 1}

def f(n):
    if n in dp:
        return dp[n]
    if n % 2 == 0:
        res = f(n//2) + f(n-1)
    else:
        res = f(n-1)
    dp[n] = res
    return dp[n]

# print(dp)
print(f(k) % p)

# РЕШЕНИЕ С ПОМОЩЬЮ ЦИКЛА ОТ НАЧАЛА ДО КОНЦА

k, p = map(int, input().split())
dp = [0] * (k+1)
dp[1] = 0

if k >= 2:
    dp[2] = 1

if k >= 3:
    for i in range(3, k+1):
        if i % 2 == 0:
            dp[i] = dp[i//2] + dp[i-1]
        else:
            dp[i] = dp[i-1]

# print(dp)
print(dp[k] % p)