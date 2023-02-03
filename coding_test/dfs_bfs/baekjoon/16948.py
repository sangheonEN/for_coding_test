"""
- 문제 정의

크기가 N×N인 체스판과 두 칸 (r1, c1), (r2, c2)가 주어진다. 데스 나이트가 (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수를 구해보자.
데스나이트 이동 가능 방향(r, c) -> (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동

- 입력 데이터
N -> 7
r1, c1 r2 c2 -> 6 6 0 1

- 출력 데이터
r1, c1 에서 r2, c2로 이동하는데, 최소 이동 횟수를 출력!

"""

from collections import deque


def bfs(r1, c1):
    # q에 뭘 저장하지? -> q에는 초기 좌표를 저장하고 이동할때마다 좌표를 다시 저장하는 업데이트 작업을 수행함.
    q = deque()
    q.append((r1, c1))
    visited[r1][c1] = True
    board[r1][c1] = 1

    # 이동 방향
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    # 격자 칸 제한
    max_row = len(board)
    max_col = len(board[0])

    while q:
        x, y = q.popleft()

        # 방향 서칭
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < max_row and ny < max_col and visited[nx][ny] == False:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
                visited[nx][ny] = True


if __name__ == "__main__":

    N = int(input())

    board = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    r1, c1, r2, c2 = map(int, input().split())

    bfs(r1, c1)

    if visited[r2][c2] == True:
        print(board[r2][c2] - 1)
    else:
        print(-1)
