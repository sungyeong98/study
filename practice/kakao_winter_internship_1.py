#2024년 1월 22일
#kakao winter internship 가장 많이 받은 선물

#문제 설명
#선물을 직접 전하기 힘들 때 카카오톡 선물하기 기능을 이용해 축하 선물을 보낼 수 있습니다. 
#당신의 친구들이 이번 달까지 선물을 주고받은 기록을 바탕으로 다음 달에 누가 선물을 많이 받을지 예측하려고 합니다.
#두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
#두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
#선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
#만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
#다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return 하도록 solution 함수를 완성해 주세요.

friends=["muzi", "ryan", "frodo", "neo"]
gifts=["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

def solution(friends,gifts):
    #서로 선물을 몇번 줬는지 횟수를 저장하기 위한 이중배열
    gift_cnt=[[0 for _ in range(len(friends))] for _ in range(len(friends))]

    #이름 인덱스값을 불러오기 위한 해시
    name_cnt={i: j for j,i in enumerate(friends)}

    #인덱스 값으로 이름을 불러오기 위한 해시
    idx={i:j for i,j in enumerate(friends)}

    #선물 지수를 저장하기 위한 배열
    gift_score=[0 for _ in range(len(friends))]

    #총 받은 선물 갯수를 저장하기 위한 배열
    total_cnt=[0 for _ in range(len(friends))]

    #gifts배열을 순회하면서 누가 누구에게 선물을 몇 번 줬는지 계산
    for log in gifts:
        i,j=log.split(' ')
        gift_cnt[name_cnt[i]][name_cnt[j]]+=1

    #준 선물 갯수와 받은 선물 갯수를 카운트, 선물 지수 계산 후 저장
    for i in friends:
        give_gift,take_gift=sum(gift_cnt[name_cnt[i]]),0
        for j in range(len(friends)):
            take_gift+=gift_cnt[j][name_cnt[i]]
        score=give_gift-take_gift
        gift_score[name_cnt[i]]=score
    
    #gift_cnt를 순회하면서 받을 선물을 카운트
    for i in range(len(friends)):
        for j in range(len(friends)):
            if i!=j:
                #서로 선물을 준 경우에 대해서 계산
                if (gift_cnt[i][j]!=0 or gift_cnt[j][i]!=0) and gift_cnt[i][j]>gift_cnt[j][i]:
                    total_cnt[i]+=1
                #서로 같은 갯수의 선물을 주고받은 경우에 대해서 계산
                elif (gift_cnt[i][j]!=0 or gift_cnt[j][i]!=0) and gift_cnt[i][j]==gift_cnt[j][i]:
                    if gift_score[i]>gift_score[j]:
                        total_cnt[i]+=1
                #서로 선물을 주지 않은 경우에 대해서 계산
                elif gift_cnt[i][j]==0 and gift_cnt[j][i]==0:
                    if gift_score[i]>gift_score[j]:
                        total_cnt[i]+=1
    return max(total_cnt)
print(solution(friends,gifts))