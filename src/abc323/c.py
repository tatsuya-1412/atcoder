n, m = map(int, input().split())
a = list(map(int, input().split()))

scores = [0] * n
not_solves = []
ans = [0] * n
for i in range(n):
    s = list(input())
    scores[i] += i + 1
    not_solve = []
    for j in range(m):
        if s[j] == "o":
            scores[i] += a[j]
        else:
            not_solve.append(j)
    not_solves.append(not_solve)

max_score = max(scores)
max_index = scores.index(max_score)

for i in range(n):
    if i == max_index:
        continue
    score = scores[i]
    a_i = [0] * len(not_solves[i])
    for j in range(len(not_solves[i])):
        a_i[j] = a[not_solves[i][j]]
    a_i.sort(reverse=True)

    for item in a_i:
        score += item
        ans[i] += 1
        if score > max_score:
            break

for item in ans:
    print(item)
