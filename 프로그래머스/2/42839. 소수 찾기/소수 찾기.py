from itertools import permutations
def solution(numbers):
    
    answer = set()
    
    #numbers 순회하면서 합치기
    for i in range(1,len(numbers)+1):
        for p in permutations(numbers,i):
            num = int(''.join(p))
            #합친 숫자가 소수이면
            if num < 2:
                continue

            prime = True

            for j in range(2, num):
                if num % j == 0:
                    prime = False
                    break
            #answer에 추가
            if prime:
                answer.add(num)
    return len(answer)