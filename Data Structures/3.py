def deposit(name, x, d):
    if name in d:
        d[name] += int(x)
    else:
        d[name] = int(x)


def withdraw(name, x, d):
    if name in d:
        d[name] -= int(x)
    else:
        d[name] = -int(x)


def balance(name, d):
    if name in d:
        return d[name]
    else:
        return 'ERROR'


def transfer(name1, name2, x, d):
    if name1 in d:
        d[name1] -= int(x)
    else:
        d[name1] = -int(x)
    if name2 in d:
        d[name2] += int(x)
    else:
        d[name2] = int(x)


def income(p, d):
    for j in d.keys():
        if d[j] > 0:
            d[j] = d[j] + int(d[j] * int(p)/100)


def main():
    bank = {}
    n = int(input())
    for i in range(n):
        query = str(input()).split(' ')
        if query[0].lower() == 'deposit':
            deposit(query[1], query[2], bank)
        elif query[0].lower() == 'withdraw':
            withdraw(query[1], query[2], bank)
        elif query[0].lower() == 'balance':
            print(balance(query[1], bank))
        elif query[0].lower() == 'transfer':
            transfer(query[1], query[2], query[3], bank)
        elif query[0].lower() == 'income':
            income(query[1], bank)


main()


