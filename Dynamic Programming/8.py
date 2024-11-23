n = int(input())
l = [[0, 0, 0]]
for i in range(n):
    l.append(list(map(int, input().split())))
dp = [[0, 0, 0] for i in range(n+1)]

dp[1][0] = l[1][0]
dp[1][1], dp[1][2] = dp[1][0] + 1, dp[1][0] + 1

if n >= 2:
    dp[2][0] = dp[1][0] + l[2][0]
    dp[2][1] = l[1][1]
    dp[2][2] = max(dp[2]) + 1

if n >= 3:
    for i in range(3, n+1):
        dp[i][0] = min(dp[i-1]) + l[i][0]
        dp[i][1] = min(dp[i-2]) + l[i-1][1]
        dp[i][2] = min(dp[i-3]) + l[i-2][2]

print(l)
print(dp)

print(min(dp[n]))



