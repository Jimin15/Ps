from collections import deque

def solution(maps):

    #세로가로 길이 선언
    n = len(maps)
    m = len(maps[0])

    #큐 선언
    q = deque()

    #동서남북 선언
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #현재 위치 큐에넣기
    q.append((0,0))

    #큐가 살아있는 동안
    while q:

        #큐에서 현재위치 꺼내기
        x, y = q.popleft()

        #동서남북 확인하기
        for i in range(4):

            #다음 위치 선언
            nx = x + dx[i]
            ny = y + dy[i]

            #다음 위치가 맵 안에 있으면
            if 0 <= nx < n and 0 <= ny < m:

                #다음 위치가 갈수있는 길이면
                if maps[nx][ny] == 1:

                    #현재 거리에서 +1 해서 다음 위치에 저장
                    maps[nx][ny] = maps[x][y] + 1

                    #다음 위치 큐에넣기
                    q.append((nx, ny))

    #오른쪽아래 끝까지 못갔으면 -1 반환
    if maps[n-1][m-1] == 1:
        return -1

    #오른쪽아래 끝까지 간 거리 반환
    return maps[n-1][m-1]