from sys import stdin 
n = int(stdin.readline().strip())
def main(n):
    ans = 1
    div = 10 ** 9 + 7
    for _ in range(n):
        a = list(map(int,stdin.readline().strip().split()))
        temp = sum(a)
        ans *= temp
    print(ans%div)
if __name__ == '__main__':
    main(n)