from collections import deque
queue = deque([])


def main():
    n = int(input())
    for i in range(1, n+1):
        g = str(input())
        if g[0] == '+':
            num = int(g[2:])
            queue.append(num)

        elif g[0] == '*':
            num = int(g[2:])
            if len(queue) % 2 == 0:
                queue.insert(len(queue) // 2, num)
            else:
                queue.insert(len(queue) // 2 + 1, num)

        elif g[0] == '-':
            print(queue.popleft())


main()