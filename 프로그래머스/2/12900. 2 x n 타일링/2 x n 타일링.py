def solution(n):
    # dp[i] = 2 x i 크기를 채우는 경우의 수
    dp = [0] * (n + 1)

    dp[1] = 1

    if n >= 2:
        dp[2] = 2

    # 마지막에 세로 타일을 놓거나 가로 타일 2개를 놓는 경우
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007

    return dp[n]