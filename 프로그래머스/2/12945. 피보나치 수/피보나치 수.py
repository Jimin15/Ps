#f(0) = 0  
#f(1) = 1
#f(n)= f(n-1) + f(n-2) 
#f(n-1) = f(n-2) + f(n-3)
#f(n-2) = f(n-3) + f(n-4)

def solution(n):
    f = [0]*(n+1)
    f[0] = 0
    f[1] = 1
    
    
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    
    return f[n]%1234567
        