from sys import stdin
from collections import defaultdict
n,m = map(int, stdin.readline().strip().split())
def main(n,m):
    sl = defaultdict(int)
    ml = defaultdict(int)
    seen = set()
    ans = 0
    for _ in range(n):
        s = stdin.readline().strip()
        s = s[3:]
        sl[s] += 1
    for _ in range(m):
        m = stdin.readline().strip()
        if m in sl.keys() and m not in seen:
            ans += sl[m]
            seen.add(m)
    print(ans)

if __name__ == '__main__':
    main(n,m)