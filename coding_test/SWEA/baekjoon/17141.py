# 연구소 2 문제
# 퍼트리는데 퍼트린 최소시간을 구해야함.
# N X N 격자고 M개의 바이러스를 퍼트릴 수 있다고 하면, 2개 있는 개수 C M 조합을 활용하여 경우의 수를 찾고
# BFS로 탐색하여 가장 빠른 시간안에 퍼뜨릴 수 있는 시간을 출력해라!
# 2개 몇개 있는지 찾고 M만큼의 배치할 수 있는 경우의 수 좌표를 구하고 탐색 시작
# 시작하는 점부터 이동할 좌표에 현재 좌표 +1을 GRAPH에 적용해 업데이트 BOARD에서 가장 큰 수를 가진 값이 전부 퍼트리는데 걸리는 시간
# 벽은 -, 바이러스를 놓은 위치는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시
from itertools import combinations
from collections import deque
import copy

def virus_coordinate(board):
    empty_arr = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                empty_arr.append([i, j])

    return empty_arr


def bfs(queue):
    global result

    graph = copy.deepcopy(board)
    # 방문 배열 만들어주고 1에 해당하는 놈들은 True로 변환 -> 재방문 못하게!
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                visited[i][j] = True
            if graph[i][j] == 2:
                graph[i][j] == 0

    # 바이러스 처음 퍼트리는 지점 visited해주고
    for x, y in queue:
        visited[x][y] = True
        # 처음 퍼트리는 virus 위치는 0으로 초기화 어차피 visited 배열에서 True해서 재방문 안함
        graph[x][y] = 0

    # 종료 조건은 queue에 남아 있는게 없고 다 퍼졌을때!
    while queue:
        # 시작점이 M개니까 그만큼 순회
        for i in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue

                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    graph[nx][ny] += 1 + graph[x][y]

    # result는 graph가 가장 큰 경우와 비교해서 작을 경우 업데이트
    result = min(result, max(max(graph)))


if __name__ == "__main__":

    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for i in range(N)]

    # print(N, M)
    # print(board)

    initial_virus_arr = virus_coordinate(board)

    virus_positions = list(combinations(initial_virus_arr, M))

    result = float("inf")

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # print(virus_positions)

    # 조합으로 구한 virus positions들을 각각 queue에 넣어서 bfs로
    for positions in virus_positions:
        queue = deque()

        for spread_position in positions:
            queue.append(spread_position)
        # M개의 초기 바이러스 position이 들어감!
        bfs(queue)

    print(result)