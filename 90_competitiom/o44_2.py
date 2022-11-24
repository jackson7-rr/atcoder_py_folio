from sys import stdin 
from collections import deque
n,q = map(int,stdin.readline().strip().split())
a = list(map(int,stdin.readline().strip().split()))
def main(n,q,a):
    sif = 0
    for i in range(q):
        t, x, y = map(int,stdin.readline().strip().split())
        x -= 1
        y -= 1
        if t == 1:
            temp = a[(x-sif)%n]
            a[(x- sif)%n] = a[(y-sif)%n]
            a[(y-sif)%n] = temp  
        elif t == 2:
            sif += 1
        else:
            print(a[(x-sif)%n])
if __name__ == '__main__':
    main(n,q,a)
