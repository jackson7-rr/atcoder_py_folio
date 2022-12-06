from sys import stdin
from collections import deque
q = int(stdin.readline().strip())
def main(q):
    deck = deque()
    for i in range(q):
        t,x = map(int, stdin.readline().strip().split())
        if t == 1:
            deck.appendleft(x)
        elif t == 2:
            deck.append(x)
        else:
            x -=1
            print(deck[x])
if __name__ == '__main__':
    main(q)