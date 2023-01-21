from sys import stdin 
n,p,q,r,s = map(int, stdin.readline().strip().split())
def main(n,p,q,r,s):
    a = list(map(int, stdin.readline().strip().split()))
    a[p-1:q], a[r-1:s] = a[r-1:s], a[p-1:q]
    print(*a)
if __name__ == '__main__':
    main(n,p,q,r,s)