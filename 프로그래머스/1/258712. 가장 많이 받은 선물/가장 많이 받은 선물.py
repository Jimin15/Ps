def solution(friends, gifts):

    # 다음 달에 받을 선물 개수
    answer = {}

    # 선물 지수
    gift_score = {}

    # 누가 누구에게 선물을 몇 개 줬는지
    gift_count = {}

    for friend in friends:
        answer[friend] = 0
        gift_score[friend] = 0
        gift_count[friend] = {}

        for other in friends:
            gift_count[friend][other] = 0

    # 기존 선물 기록 확인
    for gift in gifts:
        giver, receiver = gift.split()

        # 선물 지수 계산
        gift_score[giver] += 1
        gift_score[receiver] -= 1

        # 선물 교환 기록
        gift_count[giver][receiver] += 1

    # 두 사람씩 비교
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):

            a = friends[i]
            b = friends[j]

            # a가 b에게 더 많이 줌
            if gift_count[a][b] > gift_count[b][a]:
                answer[a] += 1

            # b가 a에게 더 많이 줌
            elif gift_count[a][b] < gift_count[b][a]:
                answer[b] += 1

            # 주고받은 개수가 같음
            else:

                # 선물 지수 비교
                if gift_score[a] > gift_score[b]:
                    answer[a] += 1

                elif gift_score[a] < gift_score[b]:
                    answer[b] += 1

    return max(answer.values())