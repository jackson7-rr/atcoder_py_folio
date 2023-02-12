from sys import stdin 
from collections import deque
n,m = map(int, stdin.readline().strip().split())
flag = [False for _ in range(n+1)]
flag[0] = True
graph = [[] for _ in range(n+1)]
d = deque()
c = 0
def dfs(v,ans):
    flag[v] = True
    for g in graph[v]:
        if flag[g] == False:
            dfs(g,ans)
    ans.append(v)
    return
def main(n,m):
    if m == 0:
            ans = [i for i in range(1,n+1)]
            print(*ans)
            exit()
    ans = []
    a = list(map(int, stdin.readline().strip().split()))
    for _ in range(n):
        for i in a:
            graph[i].append(i+1)
            graph[i+1].append(i)
    for i in range(1,n+1):
        if flag[i] == False:
            dfs(i,ans)
    print(*ans)
if __name__ == '__main__':
    main(n,m)