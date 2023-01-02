from sys import stdin 
n = int(stdin.readline().strip())
def main(n):
    ans = []
    for i in range(2**n):
        temp = str()
        lc = 0
        rc = 0
        for j in range(n):
            if (i >> j & 1):
                temp += ')'
                rc += 1
            else:
                temp += '('
                lc += 1
            if lc - rc < 0:
                break
            if lc == rc and j == n-1:
                ans.append(temp)
    ans = sorted(ans)
    print(*ans,sep='\n')
            


if __name__ == '__main__':
    main(n)