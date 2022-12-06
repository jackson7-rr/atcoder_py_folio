from sys import stdin 
n = int(stdin.readline().strip())
def main(n):
    s = list(map(int, stdin.readline().strip().split()))
    ans = []
    temp = 0
    for i in range(n):
        ans.append(s[i]-temp)
        temp += (s[i]-temp)
    print(*ans)
if __name__ == '__main__':
    main(n)
