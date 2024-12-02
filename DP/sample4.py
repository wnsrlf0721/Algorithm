#n종류의 화폐(1<=n<=100)를 조합하여 m을 완성하라(1<=m<=10000)
#합이 m이 가능하면 최소한의 값으로, 불가능하면 -1 출력
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
value=[10001]*(m+1)
value[0]=0
for money in arr:
    for j in range(money,m+1):
        if value[j-money]!=10001:
            value[j]=min(value[j],value[j-money]+1)
if value[m]==10001:
    print(-1)
else:
    print(value[m])