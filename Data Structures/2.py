def schedule():

    t = int(input())
    teachers = set(map(int, input().split()))

    r = int(input())
    rooms = set(map(int, input().split()))

    t1 = int(input())
    teachers_vacant = set(map(int, input().split()))
    r1 = int(input())
    rooms_vacant = set(map(int, input().split()))

    if teachers & teachers_vacant:
        return -1

    if not rooms_vacant - rooms:
        return -1

    teachers_new = sorted(list(teachers | teachers_vacant))

    cab = min(rooms_vacant - rooms)
    rooms.add(cab)
    new_rooms = sorted(list(rooms))

    print(len(teachers_new))
    print(' '.join(map(str, teachers_new)))
    print(len(new_rooms))
    return ' '.join(map(str, new_rooms))


print(schedule())
