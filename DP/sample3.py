# Nx2의 직사각형 바닥을 1x2, 2x1, 2x2타일 3가지를 이용해 채울 수 있는 모든 경우의 수 출력
n=int(input())
d=[0]*(n+1)
d[1],d[2]=1,3
#top-down
def top_tile(n):
    if d[n]!=0:
        return d[n]
    if d[n-1]!=0 and d[n-2]!=0:
        d[n]=d[n-1]+d[n-2]*2
        return d[n]
    return (top_tile(n-1)+top_tile(n-2)*2)%796796
#bottom-up
def bottom_tile(n):
    for i in range(3,n+1):
        d[i]=(d[i-1]+d[i-2]*2)%796796
    return d[n]
#print(top_tile(n))
print(bottom_tile(n))