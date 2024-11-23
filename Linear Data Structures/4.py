n = int(input())
wagons = list(map(int, input().split()))
st = []
expected = 1

def f(expected):
    for i in wagons:
        st.append(i)
        while st and st[-1] == expected:
            st.pop()
            expected += 1

    if expected == n+1:
        return 'YES'
    else:
        return 'NO'

print(f(expected))