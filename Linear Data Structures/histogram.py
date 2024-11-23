def histogram(h):
    h = [0] + h
    st = []
    best = 0
    for i in range(1, len(h)):
        cur = [h[i], 0, i]
        while st and st[-1][0] > cur[0]:
            st[-1][0] = st[-1][0] * st[-1][1] + st[-1][0] * (i-st[-1][2])
            if best < st[-1][0]:
                best = st[-1][0]
            cur[1] += 1 + st[-1][1]
            st.pop()
        if st and st[-1][0] == cur[0]:
            cur[1] += 1 + st[-1][1]
            st[-1][0] = 0

        st.append(cur)

    if st:
        for j in st:
            j[0] = j[0] * j[1] + j[0] * (len(h) - j[2])
            if best < j[0]:
                best = j[0]

    return best


print(histogram(list(map(int, input().split()))))