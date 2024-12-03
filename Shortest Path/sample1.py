#1~N company(node), they connected with edge(edge is bi-direction)
#person A located in 1 node, and go X node after go K (seq: 1->k->x)
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1
for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][i]+graph[i][b])
x,k=map(int, input().split())
count=graph[1][k]+graph[k][x]
if count>=INF:
    print(-1)
else:
    print(count)