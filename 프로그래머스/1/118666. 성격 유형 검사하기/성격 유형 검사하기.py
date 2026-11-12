def solution(survey, choices):
    answer = ''
    
    # 사전으로 점수 저장 {}
    score = dict()
    score['R'] = 0
    score['T'] = 0
    score['C'] = 0
    score['F'] = 0
    score['J'] = 0
    score['M'] = 0
    score['A'] = 0
    score['N'] = 0
    
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
    if score['R']>score['T']:
        answer+='R'
    elif score['R']<score['T']:
        answer+='T'
    else:
        answer+='R'

    # C,F점수 비교
    if score['C']>score['F']:
        answer+='C'
    elif score['C']<score['F']:
        answer+='F'
    else:
        answer+='C'

    # J,M점수 비교
    if score['J']>score['M']:
        answer+='J'
    elif score['J']<score['M']:
        answer+='M'
    else:
        answer+='J'

    # A,N점수 비교
    if score['A']>score['N']:
        answer+='A'
    elif score['A']<score['N']:
        answer+='N'
    else:
        answer+='A'

    
    
    return answer
