from sys import stdin 
n,k = map(int,stdin.readline().strip().split())
s = stdin.readline().strip()
def main(n,k,s):
    ans = str()
    for i in range(n):
        if s[i] == 'o' and k != 0:
            ans += 'o'
            k -= 1
        else:
            ans += 'x'
    print(ans)
if __name__ == '__main__':
    main(n,k,s)