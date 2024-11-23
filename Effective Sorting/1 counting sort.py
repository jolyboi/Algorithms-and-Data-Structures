# list1 = [1, 2, 3]
# list2 = list1  # Both list1 and list2 point to the same list
#
# list1.clear()  # Clears the list in place
#
# print(list1)   # Output: []
# print(list2)   # Output: [] (both references now show an empty list)

def solution():
    cnt = [0] * 10
    ans = []
    text = str(input())
    for char in text:
        try:
            cnt[int(char)] += 1
        except ValueError:
            continue
    for i in range(9, -1, -1):
        ans += [i] * cnt[i]
    if ans:
        return ''.join(map(str, ans))
    else:
        return -1


print(solution())
