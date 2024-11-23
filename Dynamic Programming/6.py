n = int(input())
dp = [[-1, -1, -1] for i in range(n+1)]
dp[1][0] = 1  # на ноль
dp[1][1] = 1  # на 01
dp[1][2] = 0  # на 11

def f(n):
    if -1 not in dp[n]:
        return dp[n][0] + dp[n][1] + dp[n][2]

    if n >= 2:
        dp[2][0] = 2
        dp[2][1] = 1
        dp[2][2] = 1

    if n >= 3:
        for i in range(3, n + 1):
            dp[i][0] = f(i - 1)
            dp[i][1] = dp[i - 1][0]
            dp[i][2] = dp[i - 1][1]

    return dp[n][0] + dp[n][1] + dp[n][2]



print(f(n))
