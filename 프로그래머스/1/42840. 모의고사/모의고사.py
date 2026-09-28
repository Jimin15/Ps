def solution(answers):
    a = [1, 2, 3, 4, 5]
    a_s = 0
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    bs = 0
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cs = 0
    
    for i in range(len(answers)):
        if a[i%len(a)] == answers[i]:
            a_s+=1
        if b[i%len(b)] == answers[i]:
            bs+=1
        if c[i%len(c)] == answers[i]:
            cs+=1
    
    answer = [a_s,bs,cs]
    aa = []
    
    m = max(answer)
    for i in range(len(answer)):
        if answer[i] == m:
            aa.append(i+1)
    return aa
    
