n = int(input())
h = [0] + list(map(int, input().split()))
dp = [[0, 0] for i in range(n+1)]

dp[1][0], dp[1][1] = 0, 0

if n >= 2:
    dp[2][0] = abs(h[2] - h[1])
    dp[2][1] = dp[2][0] + 1

if n >= 3:
    for i in range(3, n+1):
        dp[i][0] = abs(h[i] - h[i-1]) + min(dp[i-1])
        dp[i][1] = 3 * abs(h[i] - h[i-2]) + min(dp[i-2])

# print(h)
# print(dp)
print(min(dp[n]))
