m = int(input())
s_1 = list(map(int, input()))
s_2 = list(map(int, input()))
s_3 = list(map(int, input()))

ans = 3 * m + 1
for i in range(10):
    if (not i in s_1) or (not i in s_2) or (not i in s_3):
        continue
    f_1 = [j for j, x in enumerate(s_1) if x == i]
    f_2 = [j for j, x in enumerate(s_2) if x == i]
    f_3 = [j for j, x in enumerate(s_3) if x == i]

    if len(f_1) == 1:
        f_1.append(f_1[0] + m)
        f_1.append(f_1[0] + 2 * m)
    elif len(f_1) == 2:
        f_1.append(f_1[0] + m)
    if len(f_2) == 1:
        f_2.append(f_2[0] + m)
        f_2.append(f_2[0] + 2 * m)
    elif len(f_2) == 2:
        f_2.append(f_2[0] + m)
    if len(f_3) == 1:
        f_3.append(f_3[0] + m)
        f_3.append(f_3[0] + 2 * m)
    elif len(f_3) == 2:
        f_3.append(f_3[0] + m)

    for j in range(3):
        for k in range(3):
            for l in range(3):
                if f_1[j] == f_2[k] or f_2[k] == f_3[l] or f_3[l] == f_1[j]:
                    continue
                ans = min(ans, max(f_1[j], f_2[k], f_3[l]))

if ans == 3 * m + 1:
    ans = -1

print(ans)
