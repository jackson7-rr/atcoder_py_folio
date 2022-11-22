from sys import stdin
from collections import deque
n,k = map(int, stdin.readline().strip().split())
a = list(map(int, stdin.readline().strip().split()))
def main(n,k,a):
    d = deque(a)
    for _ in range(k):
        d.popleft()
        d.append(0)
    print(*d)
if __name__ == '__main__':
    main(n,k,a)