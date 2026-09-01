#numbers의 값을 더하거나 빼서 target값을 만들기
#횟수 더하기
#재귀로 풀기 

def solution(numbers, target):
    
   #target값이랑 같은 횟수
    answer = [0]
    
     # 재귀 횟수 변수, 현재 값
    def dfs(cnt, cur):
        
        # 재귀횟수랑 numbers의 개수랑 같으면
        if cnt==len(numbers):
        
            # 타겟값이랑 같으면 횟수더하기
            if target == cur:
                answer[0]+=1
            return 
    
        #다음재귀 플러스 orr 마이너스
        dfs(cnt+1,cur+numbers[cnt])
        dfs(cnt+1,cur-numbers[cnt])

    dfs(0,0)
    return answer[0]
   