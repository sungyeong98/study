#2022 카카오 블라인드 채용 양과 늑대

#문제 설명
#2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있습니다. 이 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다. 
#각 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다. 
#이때, 늑대는 양을 잡아먹을 기회를 노리고 있으며, 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다. 
#당신은 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.
#각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info, 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges가 매개변수로 주어질 때, 
#문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리인지 return 하도록 solution 함수를 완성해주세요.

#0=양, 1=늑대
info=[0,0,1,1,1,0,1,0,1,0,1,1]
edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

def solution(info,edges):
    answer=[]
    n=len(info)
    #각 노드의 방문을 기록하기 위한 배열
    visited=[0]*n
    #0번 노드부터 출발이기 때문에 0번 노드는 방문한 상태라고 미리 기록
    visited[0]=1
    find_sheep(1,0,edges,visited,info,answer)
    return max(answer)

def find_sheep(sheep_num,wolf_num,edges,visited,info,answer):
    #양의 수가 늑대보다 많을때만 양의 수를 바로바로 기록
    if sheep_num>wolf_num:
        answer.append(sheep_num)
    else:
        return
    for i,j in edges:
        #현재 노드가 방문한 노드이고, 다음 노드는 방문한 노드가 아닐 때
        if visited[i] and not visited[j]:
            visited[j]=1
            if info[j]==0:
                find_sheep(sheep_num+1,wolf_num,edges,visited,info,answer)
            else:
                find_sheep(sheep_num,wolf_num+1,edges,visited,info,answer)
            #늑대의 수가 더 많아져 다시 돌아왔을 때, 다음에 다시 방문할 수 있도록 방문기록을 다시 없앤다.
            visited[j]=0
print(solution(info,edges))