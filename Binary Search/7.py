def main():
    n = int(input())
    count = 0
    sides = []
    for i in range(n):
        sides.append(int(input()))
    sides.sort()
    for i in range(n-2):
        for j in range(i+1, n-1):
            l = j
            r = n
            while r - l > 1:
                m = (r+l) // 2
                if sides[m] < sides[i] + sides[j]:
                    l = m
                else:
                    r = m
            count += l - j

    return count


print(main())