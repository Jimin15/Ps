def solution(m, n, puddles):

    a = [[0] * m for _ in range(n)]
    a[0][0] = 1

    for x, y in puddles:
        a[y - 1][x - 1] = -1

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue

            if a[i][j] == -1:
                continue

            if i > 0 and a[i - 1][j] != -1:
                a[i][j] += a[i - 1][j]

            if j > 0 and a[i][j - 1] != -1:
                a[i][j] += a[i][j - 1]


    return a[n - 1][m - 1] % 1000000007