def solution(clothes):
    hash_map = {}

    # 1. 의상 종류별 개수 저장
    for _,category in clothes:
        hash_map[category] = hash_map.get(category, 0)+1

    # 2. 조합 개수 계산
    answer = 1

    for count in hash_map.values():
        answer = answer*(count+1)
        

    # 3. 아무것도 입지 않는 경우 제외
    return answer - 1
