#두 원 사이의 정수 쌍
#문제설명
#x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 두 개 주어집니다. 
#반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때, 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를 return하도록 solution 함수를 완성해주세요.
#※ 각 원 위의 점도 포함하여 셉니다.

r1,r2=2,3

#접근법은 맞은것 같은데, 일부 테스트케이스에서 오답 발생
#연산과정에서 문제가 있는것으로 판단
#보류
import math
def solution(r1,r2):
    answer=0
    for i in range(1,r2+1):
        r2_loc=math.sqrt(r2*r2-i*i)
        r2_loc=int(r2_loc)*2+1
        r1_loc=0
        if i<r1:
            r1_loc=math.sqrt(r1*r1-i*i)
            if r1_loc==int(r1_loc):
                r1_loc=r1_loc*2+1
            else:
                r1_loc=int(r1_loc)*2+1
        answer+=(r2_loc-r1_loc)
    answer*=2
    answer=answer+2*(r2-r1+1)
    return answer
print(solution(r1,r2))