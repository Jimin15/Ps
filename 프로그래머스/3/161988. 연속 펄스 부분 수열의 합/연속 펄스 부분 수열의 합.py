def solution(sequence):
    
    pulse1 = []
    pulse2 = []

    # 두 가지 펄스 수열 만들기
    for i in range(len(sequence)):
        if i % 2 == 0:
            pulse1.append(sequence[i] * 1)
            pulse2.append(sequence[i] * -1)
        else:
            pulse1.append(sequence[i] * -1)
            pulse2.append(sequence[i] * 1)
    
    current1 = pulse1[0]
    best1 = pulse1[0]

    current2 = pulse2[0]
    best2 = pulse2[0]

    for i in range(1, len(sequence)):
        current1 = max(pulse1[i], current1 + pulse1[i])
        best1 = max(best1, current1)

        current2 = max(pulse2[i], current2 + pulse2[i])
        best2 = max(best2, current2)

    return max(best1, best2)