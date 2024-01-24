#PCCP 4번 수레 움직이기

#문제설명
#퍼즐판에는 빨간색 수레와 파란색 수레가 하나씩 존재합니다. 각 수레들은 자신의 시작 칸에서부터 자신의 도착 칸까지 이동해야 합니다.
#모든 수레들을 각자의 도착 칸으로 이동시키면 퍼즐을 풀 수 있습니다.
#당신은 각 턴마다 반드시 모든 수레를 상하좌우로 인접한 칸 중 한 칸으로 움직여야 합니다. 단, 수레를 움직일 때는 아래와 같은 규칙이 있습니다.
#-수레는 벽이나 격자 판 밖으로 움직일 수 없습니다.
#-수레는 자신이 방문했던 칸으로 움직일 수 없습니다.
#-자신의 도착 칸에 위치한 수레는 움직이지 않습니다. 계속 해당 칸에 고정해 놓아야 합니다.
#-동시에 두 수레를 같은 칸으로 움직일 수 없습니다.
#-수레끼리 자리를 바꾸며 움직일 수 없습니다.

#퍼즐판의 정보를 나타내는 2차원 정수 배열 maze가 매개변수로 주어집니다. 
#퍼즐을 푸는데 필요한 턴의 최솟값을 return 하도록 solution 함수를 완성해 주세요. 
#퍼즐을 풀 수 없는 경우 0을 return 해주세요.

#0=빈칸, 1=빨간수레 시작점, 2=파란수레 시작점, 3=빨간수레 도착점, 4=파란수레 도착점, 5=벽
maze=[[4, 1, 2, 3]]

#재귀함수를 이용해서 각 케이스 별 걸리는 횟수를 구하고, 그 중 가장 작은 값을 업데이트 하는 방식으로 접근하였다.
#자세한 설명은 각 코드 줄에서 이어서 하겠다.

#최솟값을 업데이트 하기 위한 변수
min_cnt=float('inf')
#수레의 이동을 위한 변수
dx,dy=[0,0,1,-1],[-1,1,0,0]
def solution(maze):
    red_pos,blue_pos,red_end,blue_end=0,0,0,0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j]==1:
                red_pos=(i,j)
            if maze[i][j]==2:
                blue_pos=(i,j)
            if maze[i][j]==3:
                red_end=(i,j)
            if maze[i][j]==4:
                blue_end=(i,j)
    red_visited,blue_visited={red_pos},{blue_pos}
    #재귀함수를 통해서 목표지점까지 걸리는 최소횟수를 구해준다.
    dfs(red_pos,blue_pos,red_end,blue_end,red_visited,blue_visited,0,maze)

    #최솟값이 존재한다면 그 값을, 아니라면 0을 반환시켜준다.
    return min_cnt if min_cnt!=float('inf') else 0

def dfs(red_pos,blue_pos,red_end,blue_end,red_visited,blue_visited,cnt,maze):
    global min_cnt
    #각각의 말이 도착지점에 도착했을 때만 걸린 횟수를 기존의 횟수와 비교하여 업데이트를 진행하였다.
    if red_pos==red_end and blue_pos==blue_end:
        min_cnt=min(min_cnt,cnt)
        return
    
    red_list=move(red_pos,maze,red_visited,red_end)
    blue_list=move(blue_pos,maze,blue_visited,blue_end)

    for red_cp in red_list:
        for blue_cp in blue_list:
            #각 수레의 새로운 좌표가 서로 다른지, 새로운 좌표들이 기존의 좌표의 위치와 바꼈는지 확인하는 과정이다.
            if red_cp!=blue_cp and (red_cp,blue_cp)!=(blue_pos,red_pos):
                #조건을 충족한 좌표들은 집합 연산을 통해서 기록해준다
                red_new_visited=red_visited | {red_cp}
                blue_new_visited=blue_visited | {blue_cp}
                #재귀함수를 통해서 목표지점까지 탐색을 실시한다.
                dfs(red_cp, blue_cp, red_end, blue_end, red_new_visited, blue_new_visited, cnt+1, maze)

def move(pos,maze,visited,target):
    temp=[]
    #수레가 이미 도착지점이라면 다른 이동경로를 구할 필요없이 도착점만 반환시켜준다.
    if pos==target:
        return [target]
    #상하좌우 좌표값을 구하는 과정이다.
    for i in range(4):
        np=(pos[0]+dx[i],pos[1]+dy[i])
        #수레가 미로의 범위를 벗어나는지, 새로운 좌표가 이전에 방문한 곳인지, 새로운 좌표의 위치가 벽인지 확인하는 과정이다.
        if 0<=np[0]<len(maze) and 0<=np[1]<len(maze[0]) and np not in visited and maze[np[0]][np[1]]!=5:
            temp.append(np)
    #모든 조건을 충족하는 좌표값들을 리스트 형태로 반환시켜준다.
    return temp    

print(solution(maze))

#대략 2~3일 정도 소요되었다. 코드의 구성을 잡는 과정, 재귀함수를 구성하는 과정에서 오랜 시간이 소요되었다.
#재귀함수 구축 과정에서 불필요한 조건들과 복잡한 연산들이 들어가면서 무한루프 현상이 많이 발생하였다.