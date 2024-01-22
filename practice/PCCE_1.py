#2024년 1월 22일
#pccp 기출문제 1번 붕대 감기

#문제 설명
#t초 동안 붕대를 감으면서 1초동안 x만큼 체력을 회복한다. t초 연속 붕대를 감는데 성공하면 y만큼 체력을 추가로 회복한다
#대신 캐릭터의 최대체력을 넘을 수는 없다
#bandage는 기술 시전 시간, 초당 회복량, 추가 회복량
#health는 최대체력
#attacks는 공격시간, 피해량을 담은 2차원 정수 배열

bandage=[5, 1, 5]
health=30
attacks=[[2, 10], [9, 15], [10, 5], [11, 5]]
#정답 5

def solution(bandage,health,attacks):
    time,heal,bonus_heal=bandage
    max_hp,pre_attack_time=health,attacks[0][0]
    for attack_time,attack_damage in attacks:
        time_gap=attack_time-pre_attack_time-1
        if time_gap>0:
            health+=(time_gap*heal)
            health+=((time_gap//time)*bonus_heal)
            if health>max_hp:
                health=max_hp
        health-=attack_damage
        if health<=0:
            return -1
        pre_attack_time=attack_time
    return health
print(solution(bandage,health,attacks))