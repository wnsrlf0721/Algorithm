#X값을 1로 만들기 (최소 연산값 출력)
#연산은 X//5, X//3, X//2, X-1 4가지를 사용할 수 있음
#점화식 풀이 이용
#a_i = min(a_i//5, a_i//3, a_i//2, a_i-1)+1
#bottom-up
def oper(x):
    for i in range(2,x+1):
        d[i]=d[i-1]+1
        if i%5==0:
            d[i]=min(d[i],d[i//5]+1)
        if i%3==0:
            d[i]=min(d[i],d[i//3]+1)
        if i%2==0:
            d[i]=min(d[i],d[i//2]+1)
x=int(input())
d=[0]*(x+1)
oper(x)
print(d[x])