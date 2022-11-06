from sys import stdin 
n,m = map(int, stdin.readline().strip().split())
def main(n,m):
    route = [[]for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, stdin.readline().strip().split())
        route[a].append(b)
        route[b].append(a)
    route.pop(0)
    for i in range(n):
        route[i] = sorted(route[i])
        route[i].insert(0,len(route[i]))
    [print(*r) for r in route]
if __name__ == '__main__':
    main(n,m)