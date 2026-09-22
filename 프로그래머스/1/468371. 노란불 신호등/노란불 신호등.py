def solution(signals):
    limit = 1

    # 각 신호등의 전체 주기를 전부 곱함
    for g, y, r in signals:
        cycle = g + y + r
        limit *= cycle

    # 1초부터 limit초까지 확인
    for t in range(1, limit + 1):
        all_yellow = True

        for g, y, r in signals:
            cycle = g + y + r

            # 현재 신호등이 주기 안에서 몇 번째 위치인지
            pos = (t - 1) % cycle +1

            # 노란불 범위가 아니면
            if not (g < pos <= g + y):
                all_yellow = False
                break

        # 모든 신호등이 노란불이면 가장 빠른 시간이므로 바로 반환
        if all_yellow:
            return t

    return -1