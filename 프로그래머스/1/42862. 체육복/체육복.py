#lost에 잃어버린애 확인
#reserve에 있는애가 몇명 빌려 줄 수 있는지 확인
#체육복이 있는 수 리턴

def solution(n, lost, reserve):
    #reserve랑  lost동시에 있는 학생  제거
    same = set(lost) & set(reserve)

    lost = list(set(lost) - same)
    reserve = list(set(reserve) - same)
    
    #reserve에 있는애들 하나씩 반복문 돌리기
    for i in range(len(reserve)):
        #+,- 1씩해서 lost랑 매치하는 애 있는지확인
        for j in range(len(lost)):
            if (reserve[i]-1)==lost[j]:
                lost.remove(lost[j])
                break
            elif (reserve[i]+1)==lost[j]:
                lost.remove(lost[j])
                break
    return n-len(lost)
    