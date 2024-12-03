#이전 disjkstra algorithm은 start node에서 최솟값 edge를 가진 node를 찾기 위해
#linear방식으로 search 하여 O(n)의 시간이 걸리고, edge 정보 업데이트에 O(n) 시간이 걸려 총 O(n^2) time complex가 걸림
#이번 algorithm은 min heap 방식을 사용하는 heapq를 사용하여 search하는 시간을 O(logn)으로 단축하였다.
import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int, input().split()) # node a to b cost: c
    graph[a].append((b,c))
INF=int(1e9)
distance=[INF]*(n+1)
def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        heap_d,heap_c=heapq.heappop(q) #pop minimum data of heap
        if distance[heap_c]<heap_d:
            continue
        for i in graph[heap_c]:
            cost=heap_d+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(f'from {start} to {i} cost is {distance[i]}')
        
            

