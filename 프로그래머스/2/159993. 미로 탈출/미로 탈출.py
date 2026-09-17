from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])

    # 시작점, 레버, 출구 찾기
    for i in range(row):
        for j in range(col):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    # 두 지점 사이 최단거리 구하기
    def bfs(start, target):
        queue = deque()
        queue.append((start[0], start[1], 0))

        visited = [[False] * col for _ in range(row)]
        visited[start[0]][start[1]] = True

        # 상하좌우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            r, c, count = queue.popleft()

            # 목표 지점 도착
            if (r, c) == target:
                return count

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 맵 범위 안인지 확인
                if 0 <= nr < row and 0 <= nc < col:

                    # 벽이 아니고 방문하지 않은 곳
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr, nc, count + 1))

        return -1

    # 시작점에서 레버까지
    first = bfs(start, lever)

    if first == -1:
        return -1

    # 레버에서 출구까지
    second = bfs(lever, end)

    if second == -1:
        return -1

    return first + second