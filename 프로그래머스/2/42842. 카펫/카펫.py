def solution(brown, yellow):
    # 전체 격자 수
    total = brown + yellow

    # 세로 길이부터 확인
    for height in range(3, int(total ** 0.5) + 1):
        # 전체 격자 수로 나누어 떨어지는 경우만 확인
        if total % height == 0:
            width = total // height

            # 테두리를 제외한 노란색 영역 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]