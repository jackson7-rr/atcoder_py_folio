from sys import stdin 
a,b = map(int,stdin.readline().strip().split())
def main(a,b):
    ans = a ** b
    print(ans)
if __name__ == '__main__':
    main(a,b)