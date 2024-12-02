#memoization 활용: 한 번 구한 결과를 메모리 공간에 메모해두고(d[] 배열 활용) 메모한 결과를 그대로 가져오는 기법
#top-down
#재귀함수 활용: 큰 문제를 여러 작은 문제로 쪼개 문제의 답 도출
def top_fibo(x):
    print(f'{str(x)}',end=" ")
    if x==1 or x==2:
        return 1
    if d[x]!=0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
#bottom-up
#반복문 활용: 작은 문제부터 큰 문제까지 순서대로 답 도출
def bottom_fibo(x):
    d[1],d[2]=1,1
    for i in range(3,x+1):
        d[i]=d[i-1]+d[i-2]
    return d[x]

n=int(input())
d=[0]*(n+1)
#print(top_fibo(n))
print(bottom_fibo(n))