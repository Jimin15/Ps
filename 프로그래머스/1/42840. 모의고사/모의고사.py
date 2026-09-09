def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    al = len(a)
    bl = len(b)
    cl = len(c)
    aa = 0
    ba = 0
    ca = 0
    
    for i in range(len(answers)):
        if a[i%al]==answers[i]:
            aa+=1
        if b[i%bl]==answers[i]:
            ba+=1
        if c[i%cl]==answers[i]:
            ca+=1
    
    answer = [aa,ba,ca]
    m = max(answer)
    a = []
    if answer.count(m) >1:
        for i in range(3):
            if m==answer[i]:
                a.append(i+1)
        return a
    else:
        for i in range(3):
            if m==answer[i]:
                a.append(i+1)
                break
        return a
    
    