#2024년 1월 22일
#kakao winter internship 도넛과 막대 그래프

#문제 설명은 너무 길기에 생략
#간략하게 설명하면 그래프의 간선 정보가 주어졌을 때, 새로 생성된 노드 번호와 기존에 존재하던 그래프의 종류를 return
#하면 되는 문제
#그래프의 종류는 도넛 모양 그래프, 막대 모양 그래프, 8자 모양 그래프 총 3개다.

edges=[[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]

#첫번째 시도는 시간 초과 문제 발생, 답에는 문제가 없다.
#노드 탐색과정에서 문제가 발생한 것으로 추정된다.
'''
from collections import deque
def solution(edges):
    answer=[]
    max_node=max([max(num) for num in edges])
    graph,parent={i:[] for i in range(1,max_node+1)},{i:[] for i in range(1,max_node+1)}   
    for i,j in edges:
        graph[i].append(j)
        parent[j].append(i)
    root_node=0
    for i in range(1,max_node+1):
        if len(graph[i])>=2 and len(parent[i])==0:
            root_node=i

    shape1,shape2,shape3=0,0,0
    for i in graph[root_node]:
        if len(graph[i])==2:
            shape3+=1
        elif len(graph[i])==0:
            shape2+=1
        else:
            flag=bfs(i,graph)
            if flag==1:
                shape1+=1
            elif flag==2:
                shape2+=1
            else:
                shape3+=1
    return [root_node,shape1,shape2,shape3]
def bfs(node,graph):
    q=deque()
    q.append(node)
    visited=[]
    while q:
        current_node=q.popleft()
        visited.append(current_node)
        if len(graph[current_node])==2:
            return 3
        for i in graph[current_node]:
            if i in visited:
                return 1
            else:
                q.append(i)
    return 2
print(solution(edges))
'''

#dfs를 이용한 방법도 시간초과 발생
#bfs나 dfs 모두 내부적으로 연산이 오래 걸리는 과정이 있는 것으로 추정
'''
def solution(edges):
    answer=[]
    max_node=max([max(num) for num in edges])
    graph,parent={i:[] for i in range(1,max_node+1)},{i:[] for i in range(1,max_node+1)}   
    for i,j in edges:
        graph[i].append(j)
        parent[j].append(i)
    root_node=0
    for i in range(1,max_node+1):
        if len(graph[i])>=2 and len(parent[i])==0:
            root_node=i
    shape1,shape2,shape3=0,0,0
    for node in graph[root_node]:
        state=dfs(node,graph)
        if state==1:
            shape1+=1
        elif state==2:
            shape2+=1
        else:
            shape3+=1
    return [root_node,shape1,shape2,shape3]
def dfs(node,graph):
    stack=[]
    stack.append(node)
    visited=[]
    while stack:
        current_node=stack.pop()
        visited.append(current_node)
        if len(graph[current_node])==0:
            return 2
        elif len(graph[current_node])==2:
            return 3
        else:
            for next_node in graph[current_node]:
                if next_node in visited:
                    return 1
                stack.append(next_node)
    return 2
'''

#3번째 시도 성공
#탐색을 이용해야 하는 방법은 함정으로 각 그래프의 특징을 이용하면 시간초과 문제가 발생하지 않는다
#자세한 설명은 각 코드에 주석을 통해서 하겠다.
def solution(edges):
    #answer에 각각 새로 추가된 노드, 도넛모양, 막대모양, 8자모양 그래프의 정보를 저장하기 위한 형태로 구성
    answer=[0,0,0,0]

    #총 노드의 갯수
    num=max([max(n) for n in edges])

    #노드별 input, output을 저장
    graph={i:[[],[]] for i in range(1,num+1)}


    for i,j in edges:
        #노드 i에서 출발하는 노드를 기록
        graph[i][0].append(j)
        #노드 j로 도착하는 노드를 기록
        graph[j][1].append(i)
    
    #해당 부분이 이번 문제를 푸는데에 결정적인 역할을 하는 부분이다.
    #각 그래프의 형태별로 특징을 가지고 있다.
    for i in graph:
        #새롭게 추가된 노드를 구하는 과정이다. 기존에 없던 노드가 추가 된 것이기 때문에
        #해당 노드로 들어오는 노드는 없으며, 제한사항에 그래프의 합은 2 이상이라고 명시되어 있기 때문에
        #해당 노드에서 시작되는 노드는 최소 2개 이상이라는 뜻이다.
        if len(graph[i][0])>=2 and len(graph[i][1])==0:
            answer[0]=i
        
        #막대 그래프의 갯수를 구하는 과정이다. 막대 그래프는 순환하는 노드가 없이 리프 노드에 도달하면
        #해당 그래프는 종료된다. 그리고 막대 그래프의 리프노드는 한개만 존재할 것이기 때문에 
        #나가는 노드는 없으며, 들어오는 노드만 존재하는 노드의 갯수를 세어주면 된다.
        elif len(graph[i][0])==0 and len(graph[i][1])>0:
            answer[2]+=1

        #8자 모양 그래프의 갯수를 구하는 과정이다. 문제에서 설명하는 8자 모양 그래프를 보면 중심에 존재하는
        #노드에서 빠져나가는 노드는 2개, 들어오는 2개라는 것을 확인할 수 있다.
        #즉, 2개씩 빠져나오고 들어오는 노드의 갯수를 세어주면 해당 그래프의 갯수를 구할 수 있다.
        elif len(graph[i][0])>=2 and len(graph[i][1])>=2:
            answer[3]+=1
    
    #마지막 도넛 모양 그래프는 처음 구한 루트노드로부터 쉽게 도출할 수 있다. 루트노드에서 시작되는 노드의 갯수가
    #해당 문제에서의 그래프 갯수이기 때문에 루트노드가 가진 노드의 갯수에서 막대그래프 갯수, 8자모양 그래프의 갯수를
    #빼주면 도넛 모양 그래프의 갯수를 쉽게 구해줄 수 있다.
    answer[1]=len(graph[answer[0]][0])-answer[2]-answer[3]
    return answer
print(solution(edges))