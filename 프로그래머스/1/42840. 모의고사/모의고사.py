def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]

    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            scores[0] += 1
        if b[i % len(b)] == answers[i]:
            scores[1] += 1
        if c[i % len(c)] == answers[i]:
            scores[2] += 1

    m = max(scores)

    return [i + 1 for i in range(3) if scores[i] == m]