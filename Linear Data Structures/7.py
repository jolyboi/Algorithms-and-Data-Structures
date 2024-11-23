class Stack:
    def __init__(self):
        self._stack = []

    def __bool__(self):
        return bool(self._stack)

    def push(self, v):
        self._stack.append((v, min(v, self.min()) if self._stack else v))

    def pop(self):
        return self._stack.pop()[0]

    def min(self):
        return self._stack[-1][1]


class Queue:
    def __init__(self):
        self._stack1 = Stack()
        self._stack2 = Stack()

    def __bool__(self):
        return bool(self._stack1) or bool(self._stack2)

    def push(self, v):
        self._stack1.push(v)

    def pop(self):
        if not self._stack2:
            while self._stack1:
                self._stack2.push(self._stack1.pop())
        return self._stack2.pop()

    def min(self):
        return min(s.min() for s in (self._stack1, self._stack2) if s)


def main():
    q = Queue()
    for i in range(int(input())):
        a = int(input())
        if a > 0:
            q.push(a)
        else:
            print(q.min() if q else -1)
            if q:
                q.pop()

main()

