from sys import stdin
s = stdin.readline().strip()
n = len(s)
def main(s,n):
    s = 'a' + s
    ans = str()
    for i in range(1,n+1,2):
        ans += (s[i+1])
        ans += s[i]
    print(ans)       

if __name__ == '__main__':
    main(s,n)