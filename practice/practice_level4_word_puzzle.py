#2017 팁스타운 단어 퍼즐

#문제 설명
#단어 퍼즐은 주어진 단어 조각들을 이용해서 주어진 문장을 완성하는 퍼즐입니다. 
#이때, 주어진 각 단어 조각들은 각각 무한개씩 있다고 가정합니다. 
#예를 들어 주어진 단어 조각이 [“ba”, “na”, “n”, “a”]인 경우 "ba", "na", "n", "a" 단어 조각이 각각 무한개씩 있습니다.
#이때, 만들어야 하는 문장이 “banana”라면 “ba”, “na”, “n”, “a”의 4개를 사용하여 문장을 완성할 수 있지만, 
#“ba”, “na”, “na”의 3개만을 사용해도 “banana”를 완성할 수 있습니다. 
#사용 가능한 단어 조각들을 담고 있는 배열 strs와 완성해야 하는 문자열 t가 매개변수로 주어질 때, 
#주어진 문장을 완성하기 위해 사용해야 하는 단어조각 개수의 최솟값을 return 하도록 solution 함수를 완성해 주세요. 
#만약 주어진 문장을 완성하는 것이 불가능하면 -1을 return 하세요.

strs=["ba","na","n","a"]
t='banana'

#첫번째 시도, 정확성 테스트에서 일부 문제 시간초과, 효율성 테스트에서 런타임에러 발생
#단어가 최대 20000자이고 strs의 크기가 100까지로, 재귀함수를 사용한 접근 방식은 효율적이지 못한 것으로 판단된다.
'''
min_cnt=float('inf')
def solution(strs,t):
    dict={}
    for i in strs:
        start_alp=i[0]
        if start_alp not in dict:
            dict[start_alp]=[i]
        else:
            dict[start_alp].append(i)
    start_word=t[0]
    count(start_word,t,0,dict)
    return min_cnt if min_cnt!=float('inf') else -1
def count(start_word,target,cnt,dict):
    global min_cnt
    if len(target)==0:
        min_cnt=min(min_cnt,cnt)
        return
    for words in dict[start_word]:
        if len(words)<=len(target) and words==target[:len(words)]:
            new_target=target[len(words):]
            new_start_word=new_target[0] if len(new_target)>0 else ''
            count(new_start_word,new_target,cnt+1,dict)
'''


def solution(strs,t):
    dp=[0 for i in range(len(t)+1)]
    for i in range(1,len(t)+1):
        dp[i]=float('inf')
        for j in range(1,6):
            if i-j<0:
                break
            start=i-j
            if t[start:i] in strs:
                dp[i]=min(dp[i],dp[i-j]+1)
    if dp[-1]==float('inf'):
        return -1
    return dp[-1]
print(solution(strs,t))