#f(0) = 0  
#f(1) = 1
#f(n)= f(n-1) + f(n-2) 
#f(n-1) = f(n-2) + f(n-3)
#f(n-2) = f(n-3) + f(n-4)

def solution(n):
    answer = [0,1]
    
    for i in range(2,n+1):
        answer.append(answer[i-1]+answer[i-2])
        
    return answer[n]%1234567