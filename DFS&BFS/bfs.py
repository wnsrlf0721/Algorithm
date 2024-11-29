from collections import deque
def bfs(start):
    queue.append(start)
    visited[start]=True
    while queue:
        now=queue.popleft()
        print(now,end=" ")
        for i in arr[now]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

queue=deque()
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
bfs(1)