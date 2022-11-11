from sys import stdin 

def main():
    n,k = map(int, stdin.readline().strip().split())
    a = list(map(int, stdin.readline().strip().split()))
    b = list(map(int, stdin.readline().strip().split()))
    dif = 0
    for i in range(n):
        dif += abs(a[i]-b[i])
    if (k-dif) % 2 == 0 and (k-dif)>=0:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()