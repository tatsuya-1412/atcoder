s = list(map(int, input()))

flag = False
for i in range(1, 17, 2):
    if s[i] == 1:
        flag = True

if flag:
    print("No")
else:
    print("Yes")
