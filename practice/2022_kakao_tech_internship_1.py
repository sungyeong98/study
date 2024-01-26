#2022년 kakao tech internship 등산코스 정하기

#문제설명
#https://school.programmers.co.kr/learn/courses/30/lessons/118669

n=6
paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates=[1,3]
summits=[5]

#이전의 코드로, 일부 문제에서 오류가 발생하였다.
'''
from collections import defaultdict
from heapq import heappop,heappush
def solution(n,paths,gates,summits):
    summits.sort()
    set_summits=set(summits)
    graph=defaultdict(list)
    for r,c,w in paths:
        graph[r].append((c,w))
        graph[c].append((r,w))
    def query_find_min_intensity():
        heap=[]
        visited=[int(1e9)]*(n+1)
        for start in gates:
            heappush(heap,(start,0))
            visited[start]=0
        while heap:
            node,intensity=heappop(heap)
            if node in set_summits or intensity>visited[node]:
                continue
            for next_node,weight in graph[node]:
                new_intensity=max(intensity,weight)
                if new_intensity<visited[next_node]:
                    visited[next_node]=new_intensity
                    heappush(heap,(next_node,new_intensity))
        min_intensity=[0,int(1e9)]
        for summit in set_summits:
            if visited[summit]<min_intensity[1]:
                min_intensity[0]=summit
                min_intensity[1]=visited[summit]
        return min_intensity
    return query_find_min_intensity()
'''

#2번째 시도에서 성공하였다.
#문제에서 요구하는 것은 왕복루트의 가장 높은 피로도 중 낮은 피로도가 소모되는 등산루트를 구하는 것인데,
#굳이 왕복루트를 구할 것 없이, 도착지점까지 소요되는 피로도만 구해주면 된다.
from collections import defaultdict
from heapq import heappop,heappush
def solution(n,paths,gates,summits):
    #효율성 문제를 해결하기 위해 출입구와 도착지점을 해시로 변경하여 관리하였다.
    summits.sort()
    gates.sort()
    summits,gates=set(summits),set(gates)

    #각 도착지점까지 소모되는 최대 피로도를 효율적으로 기록하기 위해 dp를 사용하였다.
    dp=[float('inf')]*(n+1)

    #노드의 정보를 효율적으로 관리하기 위해 해시로 관리하였다.
    graph=defaultdict(list)

    #출입구 지점의 피로도는 0으로 변경해주었다.
    for i in range(1,n+1):
        if i in gates:
            dp[i]=0

    for s,e,w in paths:
        graph[s].append((e,w))
        graph[e].append((s,w))
    
    #피로도가 낮은 노드 순으로 불러내기 위해 heap자료형을 사용하였다.
    heap=[]
    for gate in gates:
        heappush(heap,(gate,0))

    while heap:
        node,weight=heappop(heap)
        #현재 노드가 도착점에 왔다면 continue해준다.
        if node in summits:
            continue
        #현재 피로도가 기존의 피로도보다 높다면 continue해준다.
        if weight>dp[node]:
            continue
        
        #현재 노드에서 갈 수 있는 노드를 탐색한다.
        for child_node,child_weight in graph[node]:
            #만약 자식노드가 출입구라면 continue해준다.
            if child_node in gates:
                continue

            #소요될 피로도를 계산한다.
            next_weight=max(weight,child_weight)
            #만약 소요될 피로도가 기존 자식노드의 피로도 보다 높다면 continue해준다.
            if next_weight>=dp[child_node]:
                continue

            #자식노드의 피로도를 갱신해주고, heap에 넣어준다.
            dp[child_node]=next_weight
            heappush(heap,(child_node,next_weight))
    
    #도착지점을 불러와 answer에 도착지점,피로도를 넣어주고 sort를 이용하여
    #피로도,도착지점 순으로 정렬해준다.
    answer=[]
    for summit in summits:
        temp=[]
        temp.append(summit)
        temp.append(dp[summit])
        answer.append(temp)
    answer.sort(key=lambda x:(x[1],x[0]))
    return answer[0]

print(solution(n,paths,gates,summits))