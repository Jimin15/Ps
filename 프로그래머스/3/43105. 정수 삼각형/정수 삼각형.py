def solution(triangle):
    # 00 -> 10 11 
    # 10 -> 20 21
    # 11 -> 21 22 [i+1][j] or [i+1][j+1]
    # 배열돌면서 숫자를 더하기
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1] ,triangle[i-1][j])
    
    # 마지막 행의 가장 큰 수를 리턴 
    return max(triangle[len(triangle)-1])