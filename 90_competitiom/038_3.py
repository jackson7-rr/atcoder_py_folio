from sys import stdin 
import math
a,b = map(int,stdin.readline().strip().split())

def main(a,b):
    lc = (a*b) // math.gcd(a,b)
    if lc <= 10 ** 18:
        print(lc)
    else:
        print('Large')
if __name__ == '__main__':
    main(a,b)