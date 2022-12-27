from sys import stdin 
n = int(stdin.readline().strip())
a = list(map(int,stdin.readline().strip().split()))
q = int(stdin.readline().strip())
def main(n,a,q):
    for _ in range(q):
        query = list(map(int,stdin.readline().strip().split()))
        if query[0] == 1:
            a[query[1]-1] = query[-1]
        else:
            print(a[query[1]-1])
        
if __name__ == '__main__':
    main(n,a,q)