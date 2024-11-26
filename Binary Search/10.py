def main():
    left = 1
    right = min(x, y) * n
    while right - left > 1:
        middle = (left + right) // 2
        if check(middle):
            right = middle
        else:
            left = middle
    return right


def check(max_time):
    base_time = min(x, y)
    condition = n - 1
    x_produced = (max_time - base_time) // x
    y_produced = (max_time - base_time) // y
    if x_produced + y_produced < condition:
        return False
    return True


n, x, y = map(int, input().split())
print(main())