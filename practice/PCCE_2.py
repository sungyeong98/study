#2024년 1월 22일
#pccp 기출문제 2번 석유 시추

#문제 설명
#세로길이가 n 가로길이가 m인 격자 모양의 땅 속에서 석유가 발견되었습니다. 
#석유는 여러 덩어리로 나누어 묻혀있습니다. 당신이 시추관을 수직으로 단 하나만 뚫을 수 있을 때, 
#가장 많은 석유를 뽑을 수 있는 시추관의 위치를 찾으려고 합니다. 시추관은 열 하나를 관통하는 형태여야 하며, 
#열과 열 사이에 시추관을 뚫을 수 없습니다.
#만약 시추관이 석유 덩어리의 일부를 지나면 해당 덩어리에 속한 모든 석유를 뽑을 수 있습니다. 
#시추관이 뽑을 수 있는 석유량은 시추관이 지나는 석유 덩어리들의 크기를 모두 합한 값입니다.
from collections import deque
land=[[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

#bfs를 위한 축이동 변수 설정
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(x,y,visited,land,cnt):
    q=deque()
    q.append([x,y])
    visited[x][y],count=cnt,1
    
    while q:
        current_x,current_y=q.popleft()
        for i in range(4):
            next_x,next_y=current_x+dx[i],current_y+dy[i]
            if next_x<0 or next_x>=len(land) or next_y<0 or next_y>=len(land[0]):
                continue
            if visited[next_x][next_y]==0 and land[next_x][next_y]==1:
                visited[next_x][next_y]=cnt
                q.append([next_x,next_y])
                count+=1
    return count
def solution(land):
    answer,oil,cnt = [],{},1
    rows,cols=len(land),len(land[0])
    visited=[[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]==0 or land[i][j]==1:
                oil[cnt]=bfs(i,j,visited,land,cnt)
                cnt+=1
    print(visited)
    print(oil)
    return answer
print(solution(land))
#미완성