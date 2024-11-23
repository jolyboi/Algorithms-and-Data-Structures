def rev(stack):
    if len(stack) == 1:
        return stack
    else:
        return [stack.pop()] + rev(stack)


print(rev(list(map(int, input().split()))))
