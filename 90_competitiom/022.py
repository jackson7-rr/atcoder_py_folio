from sys import stdin 
import math
import numpy as np
def main():
    a, b, c = map(int, stdin.readline().strip().split())
    g = np.gcd.reduce([a,b,c])
    a = a//g -1
    b = b//g -1
    c = c//g -1
    print(a+b+c)
if __name__ == '__main__':
    main()