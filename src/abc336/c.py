import sys

input = sys.stdin.readline

n = int(input())


cnt = 0
ans = 0
while n != 0:
    surplus = n % 5
    ans += 10**cnt * surplus * 2
    n //= 5
    cnt += 1

if ans % 10 == 0:
    tmp = ans
    minus = 12
    cnt = 2
    while True:
        tmp //= 10
        if tmp % 10 != 0:
            break
        minus += 10**cnt
        cnt += 1
    print(ans - minus)
else:
    print(ans - 2)
