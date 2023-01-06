from sys import stdin 
h,w = map(int,stdin.readline().strip().split())
def main(h,w):
    a = [list(map(int,stdin.readline().strip().split())) for _ in range(h)]
    sumh = []
    sumw = []
    ans = [[] for _  in range(h)]
    for i in range(h):
        temp = sum(a[i])
        sumh.append(temp)
    for j in range(w):
        temp = sum(an[j] for an in a)
        sumw.append(temp)
    for i in range(h):
        for j in range(w):
            ans[i].append(sumh[i] + sumw[j] - a[i][j])
    [print(*an) for an in ans ]
    #print(sumh)
    #print(sumw)
if __name__ == '__main__':
    main(h,w)