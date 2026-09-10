def solution(people, limit):
    #왼쪽포인터
    l = 0
    #오른쪽 포인터
    r = len(people)-1
    #people정렬
    people.sort()
    c=0
    
    if l==r:
        return 1
    
    #people에있는 값들을 더하 기
    while l<r:
        #더한 값이 limit보다 크면 
        if people[l] + people[r] > limit:
            r-=1
        elif people[l] + people[r] <= limit:
            l+=1
            r-=1
            c+=1
        

    return len(people)-c