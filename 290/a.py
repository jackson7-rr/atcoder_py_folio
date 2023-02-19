from sys import stdin 
n,m = map(int,stdin.readline().strip().split())
def main(n,m):
    a = list(map(int,stdin.readline().strip().split()))
    b = list(map(int,stdin.readline().strip().split()))
    ans = 0
    for i in b:
        ans += a[i-1]
    print(ans)
if __name__ == '__main__':
    main(n,m)