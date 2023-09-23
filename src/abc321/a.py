n = list(map(int, input()))

tmp = 10
is_321_like_number = True
for i in n:
    if i < tmp:
        tmp = i
    else:
        is_321_like_number = False
        break

print("Yes" if is_321_like_number else "No")
