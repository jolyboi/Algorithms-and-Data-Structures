def main():
    election1 = {}
    election2 = {}
    winners = {}
    all_presidents = set()

    n = int(input())
    for i in range(n):
        state = str(input()).split(' ')
        election1[state[0]] = [int(state[1])]
        election2[state[0]] = {}

    m = int(input())
    for i in range(m):
        vote = str(input()).split(' ')
        state = vote[0]
        president = vote[1]

        all_presidents.add(president)

        if president not in election2[state]:
            election2[state][president] = 1
        else:
            election2[state][president] += 1

    for i in election2.keys():
        winner = min(election2[i], key=lambda x: (-election2[i][x], x)) # need to fix that
        election1[i].append(winner)

    for i in election1.values():
        if i[1] not in winners:
            winners[i[1]] = i[0]
        else:
            winners[i[1]] += i[0]

    for i in all_presidents:
        if i not in winners:
            winners[i] = 0

    result = sorted(winners.items(), key=lambda x: (-x[1], x[0]))
    for i in result:
        print(f'{i[0]} {i[1]}')


main()


