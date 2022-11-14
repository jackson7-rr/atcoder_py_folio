from sys import stdin 

def main():
    n,x = map(int, stdin.readline().strip().split())
    p = list(map(int, stdin.readline().strip().split()))
    ans = p.index(x)
    print(ans+1)
if __name__ == '__main__':
    main()