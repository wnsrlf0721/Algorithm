#floyd-warshall algorithm
#모든 지점에서 다른 모든 지점까지의 최단경로를 구하는 알고리즘
#단계마다 최단거리를 갖는 node 선택 후, 해당 Node's edge를 확인하여 최단거리 테이블 갱신
#node n개 탐색 O(n), 해당 node를 거치는 모든경로를 고려 O(n^2): time complexity O(n^3)
#최단거리를 저장하는 distance를 2차원 list를 통해 정보 저장 (node 각각에 대한 최단거리 필요)
#점화식처럼 distance list를 갱신하기 때문에 dynamic programming의 일종
#D_ab=min(D_ab,D_ak+D_kb) node k를 거칠 때 기존 경로보다 작은값이 나오면 distance값 변경
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    graph[i][i]=0
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print("@",end=" ")
        else:
            print(graph[i][j],end=" ")
    print("")

