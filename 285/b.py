from sys import stdin 
n = int(stdin.readline().strip())
s = stdin.readline().strip()
def main(n,s):
    for i in range(1,n):
        ans = 0
        for j in range(n-i):
            if s[j] != s[j+i]:
                ans = j+1
            else:
                break

        print(ans)


if __name__ == '__main__':
    main(n,s)