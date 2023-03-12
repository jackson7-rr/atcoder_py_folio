
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def dfs(i, j, used):
    if i == H-1 and j == W-1:
        return 1
    res = 0
    if i < H-1 and A[i+1][j] not in used:
        res += dfs(i+1, j, used | {A[i+1][j]})
    if j < W-1 and A[i][j+1] not in used:
        res += dfs(i, j+1, used | {A[i][j+1]})
    return res

print(dfs(0, 0, {A[0][0]}))

