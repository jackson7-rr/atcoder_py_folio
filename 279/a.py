from sys import stdin 
s = stdin.readline().strip()
def main(s):
    sl = len(s)
    ans = 0
    for i in range(sl):
        if s[i] == 'v':
            ans += 1
        else:
            ans += 2
    print(ans)
if __name__ == '__main__':
    main(s)