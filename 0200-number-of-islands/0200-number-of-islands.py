from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #세로가로길이
        n = len(grid)
        m = len(grid[0])

        #동서남북
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        #방문 리스트 선언
        v = [[False] * m for _ in range(n)]

        #섬 개수 선언
        answer = 0

        #모두 방문
        for x in range(n):
            for y in range(m):

                #현재 위치가 땅이고 방문하지 않았으면
                if grid[x][y] == "1" and v[x][y] == False:

                    #섬 하나 발견
                    answer += 1

                    #큐 선언
                    q = deque()

                    #현재 위치 큐에넣기
                    q.append((x, y))

                    #현재 위치 방문처리
                    v[x][y] = True

                    #큐가 살아있는 동안
                    while q:

                        #현재 위치 꺼내기
                        cur_x, cur_y = q.popleft()

                        #동서남북 확인
                        for i in range(4):

                            #다음 위치
                            nx = cur_x + dx[i]
                            ny = cur_y + dy[i]

                            #다음 위치가 맵 안에 있으면
                            if 0 <= nx < n and 0 <= ny < m:

                                #다음 위치가 땅이고 방문하지 않았으면
                                if grid[nx][ny] == "1" and v[nx][ny] == False:

                                    #방문처리
                                    v[nx][ny] = True

                                    #다음 위치 큐에넣기
                                    q.append((nx, ny))

        #섬 개수 반환
        return answer