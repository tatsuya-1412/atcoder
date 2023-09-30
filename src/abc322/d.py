import copy


def check_all(g):
    for i in range(10):
        for j in range(10):
            if g[i][j] != 1:
                return False
    return True


def check(g):
    for i in range(10):
        for j in range(10):
            if g[i][j] > 1:
                return False
    return True


def sum(g, pi, ii, jj):
    gc = copy.deepcopy(g)
    for i in range(ii, min(10, ii + 4)):
        for j in range(jj, min(10, jj + 4)):
            gc[i][j] += pi[i - ii][j - jj]
    return gc


def rotate(p, n):
    pi = p[n]
    pic = copy.deepcopy(pi)
    for i in range(4):
        for j in range(4):
            p[n][j][4 - 1 - i] = pic[i][j]
    return


ans = "No"


def solve(g, p, n):
    global ans
    if n == 3:
        if check_all(g):
            ans = "Yes"
        return True
    for i in range(6):
        for j in range(6):
            g_new = sum(g, p[n], i, j)
            if check(g_new):
                b = solve(g_new, p, n + 1)
                if b:
                    return True
    return False


p = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(3)]
g = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        if not (3 <= i <= 6 and 3 <= j <= 6):
            g[i][j] = 1

for i in range(3):
    for j in range(4):
        a = list(input())
        for k in range(4):
            if a[k] == ".":
                p[i][j][k] = 0
            else:
                p[i][j][k] = 1

b = False
is_break = False
for _ in range(4):
    for _ in range(4):
        b = solve(g, p, 0)
        if b:
            is_break = True
            break
        rotate(p, 1)
    if is_break:
        break
    rotate(p, 2)

print(ans)
