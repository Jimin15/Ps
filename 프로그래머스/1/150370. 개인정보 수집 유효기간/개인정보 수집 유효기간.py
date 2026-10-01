def solution(today, terms, privacies):
    
    
    r_y, r_m, r_d= today.split('.')
    
    # 정보 타입, 유효기간일수 저장하는 리스트
    a = []
    
    # 정답
    answer = []
    
    # 개월수를 일수로 바꾸기
    for i in terms:
        type, mon = i.split()
        a.append([type, int(mon)*28])
    
    # 오늘 날짜에서 -> privacies날짜 뺴기 일수구하기
    # 년끼리 뺴기 뺀거에*365일 +
    # 월끼리뺴기 뺸거에 * 28일 +
    # 일끼리 빼기 뺸거에 +
    k = 0
    for i in privacies:
        k +=1
        print("k",k)
        
        # 날짜랑 타입 구하기
        date, t = i.split()

        
        # 년도 월 일 구하기
        year, month, day = date.split(".")

       
        # 총 일수 구하기
        r_day = int(r_y)*(12*28) + int(r_m)*28 + int(r_d)
        s_day = int(year)*(12*28)  + int(month)*28 + int(day)
        
        answer_day = r_day - s_day
        
    
        # 타입에 해당하는 일수보다 크면 result에 넣기
        for i in a:
            if i[0] == t:
                if int(i[1]) <= answer_day:
                    answer.append(k)
    
    
    return answer