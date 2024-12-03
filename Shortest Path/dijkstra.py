#dijkstra algorithm 구조 파악하기
#특정 node에서 다른 node로 가는 최소 cost를 구하는 알고리즘
#time complexity는 O(n^2)로 사용하기엔 부적절
#후에 priority queue를 활용해 time단축 필요
import sys
input=sys.stdin.readline
n,e=map(int,input().split()) #n: node 개수, e: edge 개수
start=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int,input().split()) #node a->b (cost c)
    graph[a].append((b,c))
visited=[False]*(n+1) # visted[n] -> have searched node n's cost
INF=int(1e9)
distance=[INF]*(n+1) #nodes cost from start node

def find_small_node():
    cost=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<cost and not visited[i]:
            cost=distance[i]
            index=i
    return index

def dijkstra(start):
    visited[start]=True
    distance[start]=0 #from start to start is 0
    for i in graph[start]: #update start node's edges
        distance[i[0]]=i[1]
    
    for _ in range(n-1):
        curr=find_small_node() #find smallest node index except visited
        visited[curr]=True
        for i in graph[curr]:
            cost=distance[curr]+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
    
dijkstra(start)
for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(f'from {start} node to {i} cost: {distance[i]}')
        
