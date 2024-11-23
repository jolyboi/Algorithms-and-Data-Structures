def brackets():
    user = input()
    st = []
    st.append(user[0])
    for i in user[1:]:
        if len(st) != 0:
            if st[-1] == '(':
                if i == ')':
                    st.pop()
                else:
                    st.append(i)
            elif st[-1] == '[':
                if i == ']':
                    st.pop()
                else:
                    st.append(i)
            elif st[-1] == '{':
                if i == '}':
                    st.pop()
                else:
                    st.append(i)
        else:
            st.append(i)

    if len(st) == 0:
        return 'yes'
    else:
        return 'no'

print(brackets())


