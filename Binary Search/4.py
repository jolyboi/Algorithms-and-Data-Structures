def main():
    n = int(input())
    if n == 1:
        return 1
    i = 0
    while 2 ** i < n:
        i += 1
    return i


print(main())