def solution(message, spoiler_ranges):
    
    # 스포일러 구간에 등장한 단어를 저장
    spoiler = set()
    
    # 스포일러가 아닌 일반 구간에 등장한 단어를 저장
    normal = set()

    # 현재 단어의 시작 인덱스
    start = 0

    # message를 단어별로 나눠서 하나씩 확인
    for word in message.split(" "):
        
        # 현재 단어의 끝 인덱스 계산
        # 예: start가 0이고 word가 "apple"이면 end는 4
        end = start + len(word) - 1

        # 현재 단어가 스포일러 범위와 겹치는지 여부
        is_spoiler = False

        # 모든 스포일러 범위를 하나씩 확인
        for i, j in spoiler_ranges:
            
            # 현재 단어 범위(start ~ end)와
            # 스포일러 범위(i ~ j)가 겹치는 경우
            if start <= j and i <= end:
                is_spoiler = True
                break

        # 스포일러 범위와 겹친 단어라면 spoiler에 저장
        if is_spoiler:
            spoiler.add(word)
        
        # 스포일러 범위와 겹치지 않았다면 normal에 저장
        else:
            normal.add(word)

        # 다음 단어의 시작 위치로 이동
        # +1은 현재 단어 끝 다음 위치
        # +1은 단어 사이의 공백
        start = end + 2

    # spoiler에는 있지만 normal에도 등장한 단어는 제외
    # 즉, 스포된 곳에서만 등장한 단어만 남김
    important_words = spoiler - normal

    # 중요한 단어의 개수 반환
    return len(important_words)