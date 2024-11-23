class Queue:
    def __init__(self):
        self.queue = []
        self.start = 0
        # self.size = len(self.queue) - self.start
    def __str__(self):
        return str(self.queue[self.start:])
    def get_size(self):
        return len(self.queue) - self.start
    def pop(self):
        if self.get_size() > 0:
            value = self.queue[self.start]
            self.start += 1
            if self.start > len(self.queue) // 2:
                self.shrink()
            return value
        else:
            return 'error'
    def front(self):
        if self.get_size() > 0:
            return self.queue[self.start]
        else:
            return 'error'
    def clear(self):
        self.queue.clear()
        self.start = 0
        return 'ok'
    def exit(self):
        return 'bye'
    def push(self, num):
        self.queue.append(num)
        return 'ok'
    def shrink(self):
        self.queue = self.queue[self.start:]
        self.start = 0


def main():
    go = True
    q = Queue()
    while go:
        user = input()
        if user[:4] == 'push' and ord(user[-1]) >= 48 and ord(user[-1]) <= 57:
            num = int(user[5:])
            print(q.push(num))
        elif user == 'size':
            print(q.get_size())
        elif user == 'pop':
            print(q.pop())
        elif user == 'front':
            print(q.front())
        elif user == 'clear':
            print(q.clear())
        elif user == 'exit':
            print(q.exit())
            go = False
        elif user == 'print':
            print(q)

# main()





