from collections import deque

d = deque([])
def push_front(n):
    d.appendleft(n)
    return 'ok'


def push_back(n):
    d.append(n)
    return 'ok'


def pop_front():
    if is_empty():
        return 'error'
    return d.popleft()


def pop_back():
    if is_empty():
        return 'error'
    return d.pop()


def front():
    if is_empty():
        return 'error'
    return d[0]


def back():
    if is_empty():
        return 'error'
    return d[-1]


def size():
    return len(d)


def clear():
    d.clear()
    return 'ok'


def exit():
    return 'bye'


def is_empty():
    if len(d) == 0:
        return True
    else:
        return False


def main():
    go = True
    while go:
        user = input()
        if user[:9] == 'push_back' and ord(user[-1]) >= 48 and ord(user[-1]) <= 57:
            num = int(user[10:])
            print(push_back(num))
        elif user[:10] == 'push_front' and ord(user[-1]) >= 48 and ord(user[-1]) <= 57:
            num = int(user[11:])
            print(push_front(num))
        elif user == 'pop_back':
            print(pop_back())
        elif user == 'pop_front':
            print(pop_front())
        elif user == 'front':
            print(front())
        elif user == 'back':
            print(back())
        elif user == 'size':
            print(size())
        elif user == 'clear':
            print(clear())
        elif user == 'exit':
            go = False
            print(exit())

main()