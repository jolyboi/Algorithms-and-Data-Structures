def main():
    left = 0
    right = stalls[-1] - stalls[0] + 1
    while right - left > 1:
        mid = (right + left) // 2
        if fit(mid):
            left = mid
        else:
            right = mid
    return left


def fit(min_dist):
    cows_left = c - 1
    positions = [stalls[i] - stalls[i - 1] for i in range(1, len(stalls))]
    cur_distance = 0
    for i in positions:
        cur_distance += i
        if cur_distance >= min_dist:
            cows_left -= 1
            cur_distance = 0
    if cows_left > 0:
        return False
    return True


n, c = map(int, input().split())
stalls = list(map(int, input().split()))
print(main())

