from sys import stdin 
h,w = map(int, stdin.readline().strip().split())
def main(h,w):
    ans = 0
    for i in range(h):
        s = stdin.readline().strip()
        ans += s.count('#')
    print(ans)
if __name__ == '__main__':
    main(h,w)