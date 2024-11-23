n, k = map(int, input().split())
lst = list(map(int, input().split()))
idx1, idx2, cur_idx1 = 0, k + 1, 0
for i in range(idx2 + 1, n):
    if lst[i - k - 1] > lst[cur_idx1]:
        cur_idx1 = i - k - 1
    if lst[cur_idx1] + lst[i] > lst[idx1] + lst[idx2]:
        idx1 = cur_idx1
        idx2 = i
print(idx1 + 1, idx2 + 1)


