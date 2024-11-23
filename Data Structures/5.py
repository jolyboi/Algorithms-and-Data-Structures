def main():
    n, m = map(int, input().split())
    words = {}
    teams = {}
    for i in range(1, n+1):
        teams[i] = 0
    for i in range(m):
        guess = str(input()).split(' ')
        team = guess[0]
        word = guess[1]
        if word not in words:
            words[word] = [team]
        else:
            words[word].append(team)

    for i in words.values():
        number = int(i[-1])
        teams[number] += 1

    result = sorted(teams.items())
    for i, j in result:
        print(j, end=' ')


main()