def solution(land):
    
    # 두번째 행 부터
    for i in range(1,len(land)):
        
        # 현재 위치의 열 빼고 더하기
        land[i][0] = land[i][0] + max(land[i-1][1] ,land[i-1][2],land[i-1][3])
        land[i][1] = land[i][1] + max(land[i-1][0] ,land[i-1][2], land[i-1][3])
        land[i][2] = land[i][2] + max(land[i-1][0] ,land[i-1][1], land[i-1][3])
        land[i][3] = land[i][3] + max(land[i-1][1] ,land[i-1][2], land[i-1][0])
        
    return max(land[-1])