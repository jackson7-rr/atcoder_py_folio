from sys import stdin 
s = stdin.readline().strip()
n = len(s)
def main(n,s):
    ans = 0
    for i in range(n):
        temp = ord(s[i])-64
        ans += temp * 26** (n-1-i)
    print(ans)
if __name__ == '__main__':
    main(n,s)