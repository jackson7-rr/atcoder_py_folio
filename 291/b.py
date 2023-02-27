from sys import stdin
n = int(stdin.readline().strip())
x = list(map(int, stdin.readline().strip().split()))
def main(n,x):
    x = sorted(x)
    ep = 4 *n 
    sx = x[n:ep]
    ans = sum(sx)/(3*n)
    print(ans)
if __name__ == '__main__':
    main(n,x)