# 연구소 바이러스가 퍼진다.
# 벽을 세워서 최대한 안전 영역을 확보하자
# 2차원 배열, bfs, 백트레킹 -> 세워본 벽을 다시 허물고 시작
# board에서 2: 바이러스 시작 위치, 1: 벽, 0: 이동가능 경로
# 벽 세우고 bfs, 벽 허물고 그 다음 칸으로 가서 다시 벽세우고 bfs, 벽 허물고를 반복
# 백트레킹으로 벽 허무는 것 구현 (재귀)
# deep copy를 활용해서 벽을 세운 뒤에 탐색할 수 있는 새로운 board를 생성함.

# 정리
# 1. 벽 세우는 것을 2차원 배열을 이중 루프문으로 i, j가 N, M 까지 완전 탐색하면서 벽을 세운다. if board[i][j] == 0 일때 board[i][j] = 1 넣어주어 벽을 세움
# 2. 재귀함수를 통해 1, 2, 3개 까지 count 변수를 1씩 늘려가면서 순차적으로 세개의 벽을 세움
# 3. 3개의 벽이 세워지면 bfs()를 수행하는데, bfs()에서는 벽이 세워진 map을 새로 deepcopy해서 저장하고 그 board에서 탐색을 수행함.
# 4. 새로운 board를 graph로 graph의 i, j 좌표를 탐색하여 바이러스 초기 위치인 2의 원소를 가진 좌표를 queue에 삽입함
# 5. queue에 있는 원소가 다 없어질때까지(바이러스 초기 좌표부터) 4방향 탐색을 수행. 이때 이동 가능하면 graph에 2를 저장하고 queue에 그 좌표를 다시 삽입함.
# 6. 격자 벗어나면 continue 조건문 적용
# 7. 반복해서 queue의 원소가 없어졌으면, 벽을 세운 새로운 graph는 바이러스가 다 퍼진 상태일 것이다. 이때 행만큼 for문을 수행하여 graph의 원소가 0인 애들의 count를 수행한다.
# 8. answer이라는 전역변수에 count의 수가 가장 큰놈을 저장한다 이러면, 모든 벽을 세우는 경우가 끝났을때 0이 가장 많은 영역의 수를 얻을 수 있다.
# 9. 좀 더 생각해서 어떻게 벽을 세웠을 때 가장 많은 영역을 나타내는지까지 출력하는 코드를 짜보자.

# 재귀함수를 이용해서 3개를 세우고 bfs를 수행하도록한다. bfs 수행 후 return을 통해

import copy
from collections import deque

def bfs():
    global answer
    # global wall_coordinate

    graph = copy.deepcopy(board)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
    cnt = 0

    for i in range(N):
        cnt += graph[i].count(0)

    answer = max(answer,cnt)


def make_wall(count):
    # global wall_coordinate

    if count == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                board[i][j] = 1
                # wall_coordinate.append([i, j])
                make_wall(count+1)
                board[i][j] = 0


if __name__ == "__main__":

    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # print(N, M)
    # print(board)
    # wall_coordinate = deque()
    answer = 0
    make_wall(0)
    print(answer)
    # print(wall_coordinate)



