from sys import stdin 
n = int(stdin.readline().strip())
def main(n):
    d = dict()
    for i in range(n):
        s = stdin.readline().strip()
        if s not in d.keys():
            d[s] = i+1
    print(*list(d.values()), sep='\n')
if __name__ == '__main__':
    main(n)