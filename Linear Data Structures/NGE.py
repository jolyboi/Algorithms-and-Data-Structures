def NGE(l):
    st = []
    res = [-1] * len(l)
    for i in range(len(l)):
        while st and l[i] > st[-1][0]:
            res[st[-1][1]] = l[i]
            st.pop()
        st.append([l[i], i])
    for i in res:
        print(i)


NGE(list(map(int, input().split())))
