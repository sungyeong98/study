#월간 코드 챌린지 시즌3 공 이동 시뮬레이션

#문제설명
#n행 m열의 격자가 있습니다. 격자의 각 행은 0, 1, ..., n-1번의 번호, 
#그리고 각 열은 0, 1, ..., m-1번의 번호가 순서대로 매겨져 있습니다. 
#당신은 이 격자에 공을 하나 두고, 그 공에 다음과 같은 쿼리들을 날리고자 합니다.
#- 열 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(0, dx))
#- 열 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(1, dx))
#- 행 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(2, dx))
#- 행 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(3, dx))
#단, 공은 격자 바깥으로 이동할 수 없으며, 목적지가 격자 바깥인 경우 공은 이동하다가 더 이상 이동할 수 없을 때 멈추게 됩니다. 
#예를 들어, 5행 × 4열 크기의 격자 내의 공이 3행 2열에 있을 때 query(3, 10) 쿼리를 받은 경우 공은 4행 2열에서 멈추게 됩니다. 
#(격자의 크기가 5행 × 4열이므로, 0~4번 행과 0~3번 열로 격자가 구성되기 때문입니다.)
#격자의 행의 개수 n, 열의 개수 m, 정수 x와 y, 그리고 쿼리들의 목록을 나타내는 2차원 정수 배열 queries가 매개변수로 주어집니다.
#n × m개의 가능한 시작점에 대해서 해당 시작점에 공을 두고 queries 내의 쿼리들을 순서대로 시뮬레이션했을 때, 
#x행 y열에 도착하는 시작점의 개수를 return 하도록 solution 함수를 완성해주세요.

n=2
m=5
x=0
y=1
queries=[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]   #0: 좌, 1: 우, 2: 위, 3: 아래


#해당 문제를 도착점을 찾는 방식으로 접근하면 시간초과가 발생하게 된다.
#접근법은 도착점에서 역으로 공을 이동시키며 시작점을 찾는 것이다.
#시작점들은 최대,최소값으로 구하여 최종적으로 사각형의 넓이를 구해주면 시작점의 갯수를 도출할 수 있다.

#근데 문제는 테스트 마지막 문제에서 틀린다.
#수정 필요
def solution(n,m,x,y,queries):
    min_x,max_x,min_y,max_y=x,x,y,y
    #쿼리를 역으로 접근하여 시도하였다.
    for query,move in queries[::-1]:
        #원래는 좌측으로 이동하는 쿼리이기 때문에, 우측(y)으로 이동시킨다.
        if query==0:
            #우측 이동이기 때문에 y의 max값을 변경해준다.
            max_y+=move
            #만약 y가 격자의 크기를 벗어났다면, m의 값을 넣어준다.
            if max_y>=m:
                max_y=m-1
            #이 경우가 중요한데, 만약 y가 왼쪽 벽에 붙어있었다면 역으로 도출했을때 가능한 위치가 이동크기만큼이 된다.
            #예시로 y가 0이고 쿼리에서 왼쪽으로 3만큼 이동하라고 했을때, 역으로 계산한다면
            #y는 0부터 3의 위치를 가질 수 있다. 이는 문제에서 명시한 공의 이동조건에 따른 것이다.
            #즉, 벽에 붙어있을 경우는 값을 갱신할 필요가 없다.
            #아래의 조건은 벽에 붙어 있지 않은 경우를 말하고 있는 것으로, y의 최소값도 같이 변경시켜주었다.
            #해당 연산으로 y의 최솟값이 격자의 크기를 벗어날 수 있긴 하지만 그런 경우는 애초에 공의 시작점이
            #존재하지 않는 경우가 될 것이기 때문에 전혀 문제가 없다.
            if min_y!=0:
                min_y+=move
        #우측이동 명령이기 때문에, 좌측으로 이동시킨다.
        elif query==1:
            min_y-=move
            if min_y<0:
                min_y=0
            if max_y!=m-1:
                max_y-=move
        #위쪽이동 명령이기 때문에, 아래로 이동시킨다.
        elif query==2:
            max_x+=move
            if max_x>=n:
                max_x=n-1
            if min_x!=0:
                min_x+=move
        #아래쪽이동 명령이기 때문에, 위로 이동시킨다.
        elif query==3:
            min_x-=move
            if min_x<0:
                min_x=0
            if max_x!=n-1:
                max_x-=move
    #값들이 범위를 벗어났다는 것은 시작점이 존재하지 않는다는 것으로 0을 반환해준다.
    if min_x>n or min_y>m or max_x<0 or max_y<0:
        return 0
    #그렇지 않은 경우는 최소최대값을 통해 사각형의 넓이를 구해주어 반환해주면 시작점의 갯수가 된다.
    return (max_x-min_x+1)*(max_y-min_y+1)
print(solution(n,m,x,y,queries))