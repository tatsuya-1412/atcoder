k = int(input())
ans = 0
ans_arr = []

a = [[0 for _ in range(10)] for _ in range(11)]
for i in range(1, 11):
    for j in range(10):
        if i == 1:
            a[i][j] = 1
        elif i == 2:
            a[i][j] = j
        else:
            if j == i - 1:
                a[i][j] = 1
            elif j >= i:
                a[i][j] = sum(a[i - 1][1:j])

ii, jj = 0, 0
diff = 0
if k < 10:
    ans = k
    print(ans)
else:
    sum = 0
    for i in range(1, 11):
        for j in range(1, 10):
            if sum + a[i][j] >= k:
                ii = i
                jj = j
                diff = k - sum
                break
            sum += a[i][j]
        else:
            continue
        break

    while True:
        ans_arr.append(jj)
        ii -= 1
        if ii == 0:
            break

        sum = 0
        for j in range(jj):
            if sum + a[ii][j] >= diff:
                jj = j
                diff = diff - sum
                break
            sum += a[ii][j]

    print(*ans_arr, sep="")
