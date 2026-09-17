class Solution:
    def floodFill(self, image, sr, sc, color):
        # 시작 위치의 원래 색
        start_color = image[sr][sc]

        # 이미 같은 색이면 바꿀 필요 없음
        if start_color == color:
            return image

        def dfs(r, c):
            # 현재 위치 색 변경
            image[r][c] = color

            # 상하좌우 확인
            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # 범위 안이고 원래 색과 같으면 계속 탐색
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                    if image[nr][nc] == start_color:
                        dfs(nr, nc)

        dfs(sr, sc)

        return image