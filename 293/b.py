from sys import stdin
n = int(stdin.readline().strip())
a = list(map(int,stdin.readline().strip().split()))
def main(n,a):
    x = [i for i in range(n+1)]
    s = set()
    s.add(0)
    for i in range(n):
        if i+1 not in s:
            s.add(a[i])
    x = set(x)
    ans = x ^ s
    ans = list(ans)
    print(len(ans))
    print(*ans)
if __name__ == '__main__':
    main(n,a)