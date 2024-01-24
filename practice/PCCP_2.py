#2024년 1월 23일
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


#첫번 째 시도, 효율성 테스트에서 2개 탈락
#불필요한 부분을 삭제할 필요가 있어보인다.
'''
dx=[-1,1,0,0]
dy=[0,0,1,-1]
from collections import deque
def solution(land):
    max_oil=0
    oil={i:0 for i in range(len(land[0]))}
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j]==1:
                loc=bfs(i,j,land)
                for k in loc:
                    oil[k]+=loc[k]
                    if oil[k]>max_oil:
                        max_oil=oil[k]
    return max_oil
def bfs(x,y,land):
    q=deque()
    q.append([x,y])
    visited=set()
    while q:
        cx,cy=q.popleft()
        if (cx,cy) not in visited:
            visited.add((cx,cy))
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]==1:
                    q.append([nx,ny])
    
    loc={i:0 for i in range(len(land[0]))}
    for i,j in visited:
        land[i][j]=len(visited)
        if loc[j]==0:
            loc[j]=len(visited)
    return loc
print(solution(land))
'''

#두번 째 시도
#기존에는 land배열에 오일의 총량을 기록하며 넘어가는 불필요한 과정을 거쳤지만,
#수정한 코드에서는 그런 과정 없이 visited 배열의 변화량을 이용하여 해시함수에 바로 적용시켰다.
#자세한 설명은 코드에서 이어서 하겠다.

#상하좌우 한칸씩 이동을 위한 배열
dx=[-1,1,0,0]
dy=[0,0,1,-1]

from collections import deque
def solution(land):
    max_oil=0
    #각 열에 대한 오일의 총량을 기록하기 위한 해시
    oil={i:0 for i in range(len(land[0]))}
    visited=set()
    for i in range(len(land)):
        for j in range(len(land[0])):
            #방문하지 않은 좌표에 대하여 bfs탐색을 진행하였다.
            if (i,j) not in visited and land[i][j]==1:
                bfs(i,j,land,visited,oil)
    for i in oil:
        max_oil=max(max_oil,oil[i])
    return max_oil
def bfs(x,y,land,visited,oil):
    q=deque()
    q.append([x,y])
    #start_num을 이용하여 탐색하기 전 방문했던 좌표의 갯수를 미리 저장하였다.
    #그리고 new_col을 이용하여 각 탐색에서 방문했던 열 좌표를 기록하였다.
    new_col,start_num=set(),len(visited)
    while q:
        cx,cy=q.popleft()
        if (cx,cy) not in visited:
            visited.add((cx,cy))
            new_col.add(cy)
            for i in range(4):
                nx,ny=cx+dx[i],cy+dy[i]
                if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]==1:
                    q.append([nx,ny])
    #oil해시에 오일량을 갱신하는 과정에서 기존에 방문한 열을 제외하기 위한 배열이다.
    col_chk=[]

    for i in new_col:
        if i not in col_chk:
            col_chk.append(i)
            #탐색을 끝낸 뒤의 visited의 좌표갯수에서 처음 visited의 좌표갯수를 빼면, 오일의 총량을 계산할 수 있다.
            #이런 방식으로 불필요한 계산을 생략하고 oil해시에 바로 오일의 총량을 바로 업데이트 시켰다.
            oil[i]+=len(visited)-start_num
print(solution(land))