from sys import stdin 
from collections import defaultdict
n, q = map(int, stdin.readline().strip().split())

def main(n,q):
    follow = defaultdict(set)
    for _ in range(q):
        t, a, b = map(int, stdin.readline().strip().split())
        if t == 1:
            follow[a].add(b)
        elif t == 2:
            if b in follow[a]:
                follow[a].remove(b)
        else:
            if b in follow[a] and a in follow[b]:
                print('Yes')
            else:
                print('No')
if __name__ == '__main__':
    main(n,q)