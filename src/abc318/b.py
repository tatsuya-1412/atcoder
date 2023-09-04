n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
area = [[0 for _ in range(100)] for _ in range(100)]
cnt = 0

for i in range(n):
    for x in range(arr[i][0], arr[i][1]):
        for y in range(arr[i][2], arr[i][3]):
            if area[x][y] == 0:
                cnt += 1
                area[x][y] = 1

print(cnt)
