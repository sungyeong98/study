#스타수얼

#문제설명
#https://school.programmers.co.kr/learn/courses/30/lessons/70130
#링크로 대체

a=[5,2,3,3,5,3]

def solution(a):
    answer=0
    n=len(a)
    a=[a[0]]+a+[a[-1]]
    chk=[-1]*(n+2)
    cnt=dict()
    for i in range(1,n+1):
        if a[i] not in cnt:
            cnt[a[i]]=0
        #현재 위치에서 앞뒤로 다른 수가 있는지 확인하는 과정이다. 다른 수가 있다면 스타 수열로 만들 수 있기 때문에
        #해시함수에 바로 기록하여 관리하였다.
        if a[i-1]!=a[i] and chk[i-1]!=a[i]:
            chk[i-1]=a[i]
            cnt[a[i]]+=1
        elif a[i+1]!=a[i] and chk[i+1]!=a[i]:
            chk[i+1]=a[i]
            cnt[a[i]]+=1
        print(cnt)
        #해시함수에 기록한 갯수에 2배를 해주는 이유는 문제에서 스타수열의 길이는 2이상이라고 명시되어 있다.
        #만약 1이라는 숫자가 1번 사용되었다면, 스타수열의 길이는 1과 임의의 숫자를 포함한 길이 2의 수열이 될 것이기
        #때문에 2배를 해주었다.
        answer=max(answer,2*cnt[a[i]])
    return answer
print(solution(a))