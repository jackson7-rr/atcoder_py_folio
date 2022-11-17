from sys import stdin 
h, w = map(int, stdin.readline().strip().split())
def main(h,w):
    ans = 0
    if h == 1 or w == 1:
        print(h*w)
    else:
        ans = ((h+1)//2) * ((w+1)//2)
        print(ans)
if __name__ == '__main__':
    main(h,w)