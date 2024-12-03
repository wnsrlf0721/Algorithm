# total n nodes
import sys
import heapq
input=sys.stdin.readline
n,m,c=map(int,input().split()) #n: nodes(<=30,000) m: edges(<=200,000) c: starting node
graph=[[] for _ in range(n+1)]
INF=int(1e9)
distance=[INF]*(n+1) # edge c -> ? cost
for _ in range(m):
    x,y,z=map(int,input().split()) #edge x->y cost z
    graph[x].append((y,z)) 

def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        dist,cur=heapq.heappop(q)
        if distance[cur]<dist:
            continue
        for i in graph[cur]:
            cost=dist+i[1]
            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)
total=0
count=0
for i in range(1,n+1):
    if distance[i]==INF or distance[i]==0:
        continue
    else:
        total+=1
        count=max(count,distance[i])
print(total, count)
