import math

n = int(input())
m = int(math.ceil(math.log2(n)))
print(m)

for i in range(m):
    juice = []
    for j in range(n):
        b = format(j, f"0{m}b")
        if b[-i - 1] == "1":
            juice.append(j + 1)
    print(len(juice), *juice)

s = input()
ans = int(s[::-1], 2) + 1
print(ans)
