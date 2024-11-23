st = []
user = ' '

def size():
        print(len(st))

def push():
    num = int(user[5:])
    st.append(num)
    print('ok')

def pop():
    if len(st) == 0:
        print('error')
    else:
        print(st.pop())

def back():
    if len(st) == 0:
        print('error')
    else:
        print(st[-1])

def clear():
        st.clear()
        print('ok')

def exit():
    print('bye')

while user != 'exit':
    user = input()
    if user[:4] == 'push' and ord(user[-1]) >= 48 and ord(user[-1]) <= 57:
        push()
    elif user == 'size':
        size()
    elif user == 'pop':
        pop()
    elif user == 'back':
        back()
    elif user == 'clear':
        clear()
    elif user == 'exit':
        exit()