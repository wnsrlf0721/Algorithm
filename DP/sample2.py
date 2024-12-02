#food[] 내에서 인접 구역으로 이동하지 않고 최댓값을 얻는 방법 탐색
# [1,3,1,5]라 하면 3과 5를 선택해 8의 최댓값을 출력 
n=int(input())
food=list(map(int,input().split()))
max_val=[0]*(n+1)
for i in range(2):
    max_val[i]=food[i]

#top-down
def top(x):
    if max_val[x]!=0:
        return max_val[x]
    return max(top(x-2)+food[x],top(x-1))

#bottom-up
def bottom():
    for i in range(2,n):
        max_val[i]=max(max_val[i-1],max_val[i-2]+food[i])
    return max_val[n-1]

#print(top(n-1))
print(bottom())