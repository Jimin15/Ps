def solution(sizes):
    
    w = []
    h = []
    
    # 가로로 큰 숫자 몰아주기
    # 세로로 작은 숫자 몰아주기 
    for i,j in sizes:
        if i > j:
            w.append(i)
            h.append(j)
        else:
            h.append(i)
            w.append(j)

        
    return max(h)*max(w)