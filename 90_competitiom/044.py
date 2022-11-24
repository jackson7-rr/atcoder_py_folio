from sys import stdin
from collections import deque
n, q = map(int,stdin.readline().strip().split())
a = list(map(int,stdin.readline().strip().split()))
a = deque(a)
for i in range(q):
    t, x, y = map(int,stdin.readline().strip().split())
    if t == 1:
        a[x-1], a[y-1] = a[y-1], a[x-1]
    elif t == 2:
        a.rotate()
    else:
        print(a[x-1])