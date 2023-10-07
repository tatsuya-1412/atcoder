n = int(input())

wins = [0] * n
for i in range(n):
    s = list(input())
    win = 0
    for si in s:
        if si == "o":
            win += 1
    wins[i] = win

i_list = sorted(range(len(wins)), key=wins.__getitem__, reverse=True)
ans = [x + 1 for x in i_list]

print(*ans)
