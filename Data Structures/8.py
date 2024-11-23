def main():
    n = int(input())
    castles = []
    lines = set()
    for i in range(n):
        x, y = map(int, input().split())
        castles.append((x, y))
    castles.sort()
    for i in range(len(castles)-1):
        x = castles[i][0]
        y = castles[i][1]
        if x == castles[i+1][0]:
            lines.add(('y', castles[i+1][1]))
        else:
            lines.add(('x', castles[i+1][0]))

    print(len(lines))
    for i in lines:
        print(i[0], i[1])


main()



