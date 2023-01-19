from sys import stdin 
n = int(stdin.readline().strip())
a = list(map(int,stdin.readline().strip().split()))
b = list(map(int,stdin.readline().strip().split()))
a = sorted(a)
b = sorted(b)
def main(a,b,n):
    ans = 0
    for i in range(n):
        ans += abs(a[i]-b[i])
    print(ans)
if __name__ == '__main__':
    main(a,b,n)