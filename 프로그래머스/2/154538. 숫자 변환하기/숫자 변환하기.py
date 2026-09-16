def solution(x, y, n):
    dp = [-1] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):

        if dp[i] == -1:
            continue

        # i + n
        if i + n <= y:
            if dp[i + n] == -1:
                dp[i + n] = dp[i] + 1
            else:
                dp[i + n] = min(dp[i + n], dp[i] + 1)

        # i * 2
        if i * 2 <= y:
            if dp[i * 2] == -1:
                dp[i * 2] = dp[i] + 1
            else:
                dp[i * 2] = min(dp[i * 2], dp[i] + 1)

        # i * 3
        if i * 3 <= y:
            if dp[i * 3] == -1:
                dp[i * 3] = dp[i] + 1
            else:
                dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    return dp[y]