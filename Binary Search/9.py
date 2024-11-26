def main():
    left = max(pages)
    right = sum(pages)
    while right - left > 1:
        middle = (right + left) // 2
        if can_divide(middle):
            right = middle
        else:
            left = middle

    return right

def can_divide(max_pages):
    tomes = 1
    cur_count = 0
    for i in pages:
        if cur_count + i > max_pages:
            tomes += 1
            cur_count = i
            if tomes > k:
                return False
        else:
            cur_count += i
    return True


n = int(input())
pages = list(map(int, input().split()))
k = int(input())
print(main())

