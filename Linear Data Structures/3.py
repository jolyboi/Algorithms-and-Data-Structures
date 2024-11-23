user = list(map(str, input().split()))
st = []
res = 0
def mult():
    res = st.pop()
    res *= st.pop()
    st.append(res)
def plus():
    res = st.pop()
    res += st.pop()
    st.append(res)
def minus():
    res = -st.pop()
    res += st.pop()
    st.append(res)
def calculation(user):
    for i in user:
        if i == '+':
            plus()
        elif i == '-':
            minus()
        elif i == '*':
            mult()
        else:
            st.append(int(i))

    return st[-1]

print(calculation(user))