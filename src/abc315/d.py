h, w = map(int,input().split())
c = [['' for _ in range(w)] for 
     _ in range(h)]
x = [[0 for _ in range(w)] for _ in range(26)]
y = [[0 for _ in range(h)] for _ in range(26)]

for i in range(h):
    c[i] = list(input())

for i in range(h):
    for j in range(w):
        x[ord(c[i][j])-ord('a')][j] += 1
        y[ord(c[i][j])-ord('a')][i] += 1

wt = w
ht = h
bx = [False for _ in range(w)]
by = [False for _ in range(h)]
for _ in range(w+h):
    ux = []
    uy = []
    for i in range(w):
        for j in range(26):
            if bx[i]: continue
            if x[j][i] == ht and ht >= 2:
                ux.append((i,j))
    for i in range(h):
        for j in range(26):
            if by[i]: continue
            if y[j][i] == wt and wt >= 2:
                uy.append((i,j))
    for (p,q) in ux:
        bx[p] = True
        for i in range(h):
            y[q][i] -= 1
        wt -= 1
    for (p,q) in uy:
        by[p] = True
        for i in range(w):
            x[q][i] -= 1
        ht -= 1

ans = wt*ht
print(ans)