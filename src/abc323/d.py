import sys
from collections import deque


def bin_list(n):
    binary_str = bin(n)[2:]
    binary_array = [0] * len(binary_str)
    for i in range(len(binary_str)):
        binary_array[i] = int(binary_str[len(binary_str) - i - 1])

    return binary_array


input = sys.stdin.readline

n = int(input())
dic = {}
over = deque()
total = 0
for i in range(n):
    s, c = map(int, input().split())
    if c == 1:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
            over.append(s)
        total += 1
    else:
        b = bin_list(c)
        for i in range(len(b)):
            if b[i] == 1:
                ss = s * (2**i)
                if ss not in dic:
                    dic[ss] = 1
                else:
                    dic[ss] += 1
                    over.append(ss)
                total += 1

while True:
    if not len(over):
        break
    s = over.popleft()
    c = dic[s]
    dic[s] = 0
    b = bin_list(c)
    total -= c
    for i in range(len(b)):
        if b[i] == 1:
            ss = s * (2**i)
            if ss not in dic:
                dic[ss] = 1
            else:
                if dic[ss] == 0:
                    dic[ss] = 1
                else:
                    dic[ss] += 1
                    over.append(ss)
            total += 1

print(total)
