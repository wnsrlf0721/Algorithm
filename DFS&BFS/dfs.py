def dfs(start):
    visited[start]=True
    print(start, end=" ")
    for line in arr[start]:
        if not visited[line]:
            dfs(line)
arr=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited=[False]*len(arr)
dfs(1)
        