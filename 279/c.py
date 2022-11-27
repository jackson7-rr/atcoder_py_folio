from sys import stdin
from collections import Counter
h, w = map(int,stdin.readline().strip().split())
def main(h,w):
    s = [list(stdin.readline().strip()) for i in range(h)]
    t = [list(stdin.readline().strip()) for i in range(h)]
    s = [str(ss) for ss in zip(*s)]
    t = [str(tt) for tt in zip(*t)]
    sl = Counter(s)
    tl = Counter(t)
    if sl == tl:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    main(h,w)