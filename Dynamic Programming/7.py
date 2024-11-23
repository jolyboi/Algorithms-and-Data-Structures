# n = int(input())
# gvozd = [-1] + list(map(int, input().split()))
# dp = [[-1, -1] for i in range(n+1)] # distance and side of attachment
#
# def f(n):
#     if -1 not in dp[n]:
#         return dp[n][0]
#     else:
#         dp[1][0], dp[2][0] = gvozd[2] - gvozd[1], gvozd[2] - gvozd[1]
#         dp[1][1] = 1
#         dp[2][1] = 0
#         if n >= 3:
#             for i in range(3, n+1):
#                 diff = (gvozd[i] - gvozd[i-1])
#                 if i != n:
#                     if dp[i-2][1] == 1: # if attached
#                         dp[i][0] = f(i-1) + diff
#                         dp[i][1] = 0
#                     else:               # if not attached
#                         if diff <= gvozd[i-1] - gvozd[i-2]:
#                             dp[i-1][1] = 1
#                             dp[i][0] = f(i-2) + diff
#                             dp[i][1] = 0
#                         else:
#                             dp[i][0] = f(i-2) + diff
#                             dp[i][1] = 0
#                 else:
#                     if dp[i-2][1] == 1:
#                         dp[i][0] = f(i-1) + diff
#                     else:
#                         dp[i][0] = f(i-2) + diff
#
#
#         return dp[n][0]
#
# print(f(n))

# n = int(input())
# gvozd = [-1] + list(map(int, input().split()))
# dp = [[-1, -1] for i in range(n+1)]
# distance = 0
# gvozd.sort()
#
# def f(n, gvozd, distance):
#
#     dp[1][0] = gvozd[2] - gvozd[1]  # 1
#     dp[1][1] = 1
#
#     dp[2][0] = gvozd[2] - gvozd[1] # 2
#     dp[2][1] = 0
#
#     if n > 2:
#         dp[n-1][0] = gvozd[n] - gvozd[n-1] # n-1
#         dp[n-1][1] = 1
#
#         dp[n][0] = gvozd[n] - gvozd[n-1]  # n
#         dp[n][1] = 0
#
#     if n > 4:
#         for i in range(3, n-1):
#             if dp[i-1][1] == 1:
#
#                 dp[i][0] = dp[i-1][0]
#                 dp[i][1] = 0
#
#             else:
#
#                 if gvozd[i] - gvozd[i-1] < gvozd[i+1] - gvozd[i]:
#                     dp[i][0] = gvozd[i] - gvozd[i-1]
#                     dp[i][1] = 0
#                 elif gvozd[i] - gvozd[i-1] > gvozd[i+1] - gvozd[i]:
#                     dp[i][0] = gvozd[i+1] - gvozd[i]
#                     dp[i][1] = 1
#                 else:
#                     if dp[i-1][1] == 0:
#                         dp[i][0] = gvozd[i+1] - gvozd[i]
#                         dp[i][1] = 1
#                     else:
#                         dp[i][0] = gvozd[i] - gvozd[i-1]
#                         dp[i][1] = 0
#
#
#     distance += dp[1][0]
#     for i in range(2, n):
#         if not (dp[i-1][1] == 1 and dp[i][1] == 0):
#             distance += dp[i][0]
#
#
#     if not (dp[n-1][1] == 1 and dp[n][1] == 0):
#         distance += dp[n][0]
#
#     # print(dp)
#     # print(distance)
#     return distance
#
# print(f(n, gvozd, distance))
#


n = int(input())
p = [0] + sorted(list(map(int, input().split())))
dp = [0] * (n+1)

def f(n):

    dp[1] = p[1]
    dp[2] = p[2] - p[1]

    if n >= 3:
        dp[3] = p[3] - p[1]
        if n >= 4:
            for i in range(4, n+1):
                dp[i] = p[i] - p[i-1] + min(dp[i-1], dp[i-2])


    return dp[n]



print(f(n))


















