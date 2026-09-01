

# 노드가 연결되어있는거 세기
# 각 computers를 돌면서 방문한 노드는 visitor에 넣기
# 다른 노드를 방문했을 때 나랑 연결되어있으면 진행
# 연결되어 있지않으면 +=1

def solution(n, computers):
    
    answer = 0
    
    #방문여부 리스트
    visitor = [False]*n
    
    #지금 방문노드
    def dfs(node):
        # 방문여부 리스트에 자신의 노드추가
        visitor[node] = True
        
        # 자기 자신 열을 돌면서 1을 찾기
        for i in range(n):
            if computers[node][i]==1 and not visitor[i]:
                dfs(i)
    
    for i in range(n):
        if not visitor[i]:
            dfs(i)
            answer+=1
    
    return answer
        
        
    
    
    
