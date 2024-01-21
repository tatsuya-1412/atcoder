import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())

pos = deque([(i + 1, 0) for i in range(n)])

for _ in range(q):
    a, b = input().split()
    if a == "1":
        if b == "R":
            tmp = (pos[0][0] + 1, pos[0][1])
        elif b == "L":
            tmp = (pos[0][0] - 1, pos[0][1])
        elif b == "U":
            tmp = (pos[0][0], pos[0][1] + 1)
        else:
            tmp = (pos[0][0], pos[0][1] - 1)
        pos.pop()
        pos.appendleft(tmp)
    else:
        print(*pos[int(b) - 1])


## c++
# #include <iostream>
# #include <deque>

# using namespace std;

# int main() {
#     ios::sync_with_stdio(false);
#     cin.tie(NULL);

#     int n, q;
#     cin >> n >> q;

#     deque<pair<int, int>> pos;
#     for (int i = 1; i <= n; ++i) {
#         pos.push_back({i, 0});
#     }

#     for (int i = 0; i < q; ++i) {
#         int a;
#         string b;
#         cin >> a >> b;

#         if (a == 1) {
#             if (b == "R") {
#                 pair<int, int> tmp = {pos.front().first + 1, pos.front().second};
#                 pos.pop_back();
#                 pos.push_front(tmp);
#             } else if (b == "L") {
#                 pair<int, int> tmp = {pos.front().first - 1, pos.front().second};
#                 pos.pop_back();
#                 pos.push_front(tmp);
#             } else if (b == "U") {
#                 pair<int, int> tmp = {pos.front().first, pos.front().second + 1};
#                 pos.pop_back();
#                 pos.push_front(tmp);
#             } else {
#                 pair<int, int> tmp = {pos.front().first, pos.front().second - 1};
#                 pos.pop_back();
#                 pos.push_front(tmp);
#             }
#         } else {
#             int index = stoi(b) - 1;
#             cout << pos[index].first << " " << pos[index].second << "\n";
#         }
#     }

#     return 0;
# }
