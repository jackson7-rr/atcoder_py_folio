from sys import stdin 
n,k = map(int,stdin.readline().strip().split())
a = list(map(int,stdin.readline().strip().split()))
def main(n,k,a):
    check = [False for _ in range(k)]
    for i in range(n):
        if a[i] < k:
            if check[a[i]] == False:
                check[a[i]] = True
    if False not in check:
        print(k)
    else:
        print(check.index(False))  
if __name__ == '__main__':
    main(n,k,a)