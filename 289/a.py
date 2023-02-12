from sys import stdin 
s = stdin.readline().strip()
def main(s):
    ans = str()
    for i in range(len(s)):
        if s[i] == '0':
            ans += '1'
        else:
            ans += '0'
    print(ans)
if __name__ == '__main__':
    main(s)