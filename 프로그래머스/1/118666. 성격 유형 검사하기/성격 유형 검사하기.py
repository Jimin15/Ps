def solution(survey, choices):
    
    
    # 사전으로 점수 저장 {}
    score = {c: 0 for c in "RTCFJMAN"}
    
    answer = ''
    
    # 설베이를 돌기
    for i in range(len(survey)):
        
        # 초이스의 값이 1~3인경우
        if 1<=choices[i]<=3:
            score[survey[i][0]] += 4-choices[i]
       
        # 초이스의 값이 5~7인 경우
        if 5<=choices[i]<=7:
            # 오른쪽 문자에 + 초이스 값
            score[survey[i][1]] += choices[i]-4
    
    
    # R,T점수 비교
    for a, b in ['RT', 'CF', 'JM', 'AN']:
        if score[a] >= score[b]:
            answer += a
        else:
            answer += b

    
    
    return answer
