N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

i = 0
j = 0
ibest = 0
jbest = 0
goi = True
# go_i = True

while goi:
    d = abs(n[i] - m[j])
    if d < abs(n[ibest] - m[jbest]):
        ibest = i
        jbest = j

    if n[i] > m[j]:
        if j < M-1:
            j += 1
        else:
            goi = False

    elif n[i] < m[j]:
        if i < N-1:
            i += 1
        else:
            goi = False

    else:
        ibest = i
        jbest = j
        goi = False

print(n[ibest], m[jbest])











