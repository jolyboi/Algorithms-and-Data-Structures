n, k = map(int, input().split())
dp = [[-1, -1] for i in range(n+1)]
dp[1][0] = 1
dp[1][1] = k - 1

def f(n, k):

    if -1 not in dp[n]:
        return [dp[n][0], dp[n][1]]

    else:
        if n >= 2:
            for i in range(2, n+1):
                dp[i][0] = f(i-1, k)[1]           # dp[i-1][1]
                dp[i][1] = sum(f(i-1, k)) * (k-1)                  # (dp[i-1][0] + dp[i-1][1]) * (k-1)

    return dp[n][0] + dp[n][1]

print(f(n, k))



