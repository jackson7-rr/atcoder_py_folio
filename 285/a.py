from sys import stdin 
a,b = map(int,stdin.readline().strip().split())
def main(a,b):
    if b == 2 * a or b == 2 * a + 1:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main(a,b)