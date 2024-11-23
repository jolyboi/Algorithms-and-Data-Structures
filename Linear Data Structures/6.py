import Queue
def pianitsa():
    q1 = Queue.Queue()
    q2 = Queue.Queue()
    count = 0
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    for i in num1:
        q1.push(i)
    for j in num2:
        q2.push(j)
    while q1.get_size() > 0 and q2.get_size() > 0 and count < 10**6:
        c1 = q1.pop()
        c2 = q2.pop()
        if c1 == 0 and c2 == 9:
            q1.push(c1)
            q1.push(c2)
        elif c1 == 9 and c2 == 0:
            q2.push(c1)
            q2.push(c2)
        elif c1 > c2:
            q1.push(c1)
            q1.push(c2)
        elif c2 > c1:
            q2.push(c1)
            q2.push(c2)
        count += 1
    if q1.get_size() == 0:
        return 'second ' + str(count)
    elif q2.get_size() == 0:
        return 'first ' + str(count)
    else:
        return 'botva'


print(pianitsa())

