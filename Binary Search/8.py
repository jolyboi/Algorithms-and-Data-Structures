def main():
    w, h, n = map(int, input().split())
    left = 0
    right = w * n
    while right - left > 1:
        middle = (left + right) // 2
        if (middle // w) * (middle // h) < n:
            left = middle
        else:
            right = middle

    return right


print(main())