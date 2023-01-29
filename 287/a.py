from sys import stdin 
from decimal import Decimal, ROUND_HALF_UP
n = int(stdin.readline().strip())

def main(n):
    nl = n /2
    nl = Decimal(nl).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    nl = int(nl)
    ans = 0
    for i in range(n):
        s = stdin.readline().strip()
        if s == 'For':
            ans += 1
    if ans >= nl:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main(n)