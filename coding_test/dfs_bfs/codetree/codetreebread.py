"""
문제 정의
- 빵을 구하고자 하는 m명의 사람이 있는데, 1번 사람은 정확히 1분에, 2번 사람은 정확히 2분에, ..., m번 사람은 정확히 m 분에 각자의 베이스캠프에서 출발하여 편의점으로 이동
- 사람들은 출발 시간이 되기 전까지 격자 밖에 나와있으며, 사람들이 목표로 하는 편의점은 모두 다름
- n*n 크기의 격자 위에서 진행
- 이 3가지 행동은 총 1분 동안 진행되며, 정확히 1, 2, 3 순서로 진행되어야 함에 유의
- ↑, ←, →, ↓ 의 우선 순위

풀이 구상
0. 개별적으로 사람은 원하는 편의점이 1:1 매칭되어 있다.
1. 격자에서 베이스 캠프와 편의점을 이동할 수 있는지 없는지에 대한 visited list 선언
2. 1분마다 베이스 캠프로 사람이 들어오는데, 만약 거리가 같을 경우, 행 또는 열의 index기준으로 작은 쪽으로 베이스캠프를 선택해서 들어옴

입력 데이터

5 3 # n 격자칸 수, m 사람 수
0 0 0 0 0 # 격자 칸 -> 베이스캠프 1, 길 0
1 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 1
2 3 편의점 1 좌표
4 4 편의점 2 좌표
5 1 편의점 3 좌표

편의점 좌표는 index 1부터 시작! 0부터 아니고!

출력 데이터
- 모든 사람이 편의점에 도착하는 시간을 출력
- 어떠한 사람이 원하는 편의점에 도달하지 못하게 되는 경우는 절대 발생하지 않음을 가정 가능
- 동일한 칸에 둘 이상의 사람이 위치하게 되는 경우 역시 가능

고찰
일반적으로 2차원 격자에서 최단거리를 찾는 문제를 일반적으로 이런 메커니즘으로 푸시나요?

- x, y 초기 좌표 (queue에 저장)
- dx, dy 이동 좌표
- board는 0으로 초기화되어 있음
if 방문 조건에 맞을때,
    board[dx][dy] = board[x][y] + 1 으로 이전 시점에서 1칸 옮겨왔다는 걸 board에 1씩 더해서 저장
    queue.append(dx, dy) -> 다음 초기 시점 업데이트

이렇게 loop 돌면서 만약 최종 지점 x', y'에 왔을때 board[x'][y']에 저장된 값을 구하면 초기 시점부터 최종 지점까지의 최단 거리가 나오게 되겠죠?

"""

from collections import deque
import sys

def is_pass(x, y):

    return in_matrix_range(x, y) and visited_map[x][y] == False and board[x][y] != 2

def in_matrix_range(x, y):

    return x > -1 and y > -1 and x < max_row and y < max_col

def bfs(start_pos):
    # visited, step map을 전부 초기화
    for i in range(n):
        for j in range(n):
            visited_map[i][j] = False
            step_map[i][j] = 0

    # 초기 위치 q에 넣기
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited_map[sx][sy] = True
    step_map[sx][sy] = 0

    # bfs 진행
    while q:
        x, y = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if is_pass(nx, ny):
                visited_map[nx][ny] = True
                step_map[nx][ny] = step_map[x][y]+1
                q.append([nx, ny])


def simulation():

    # step 1. 격자 위의 사람들에 한해서 편의점으로 1칸씩 이동

    for i in range(m):
        # 사람이 격자 바깥에 있거나 or 편의점에 도착한 사람이면 continue
        if people[i] == empty or convenient[i] == people[i]:
            continue

        # 원래는 현재 위치에서 편의점 위치까지의 최단거리를 구해줘야 합니다.
        # 다만 최단거리가 되기 위한 그 다음 위치를 구하기 위해서는
        # 거꾸로 편의점 위치를 시작으로 현재 위치까지 오는 최단거리를 구해주는 것이 필요합니다.
        # 따라서 편의점 위치를 시작으로 하는 BFS를 진행합니다.

        bfs(convenient[i])

        # 여기까지하면, i사람 기준으로 편의점 좌표를 시작점으로 bfs 탐색을 돌려 map을 모두 방문하여 각 좌표에 최단거리를 계산한 step_map을 얻는다.
        # 그러면, i사람의 좌표에서 step_map의 상좌우하 우선순위로 인접한 영역을 탐색하면서 저장되어 있는 i편의점까지의 최단거리를 비교하여 최단거리를 특정할 수 있다.
        px, py = people[i]

        min_dist = sys.maxsize
        min_cor_x, min_cor_y = 0, 0
        # 상좌우하 우선순위로 인접한 영역을 탐색하면서 step_map에 저장되어 있는 i편의점까지의 최단거리 값을 가지고 한 칸이동을 어디로 해야할지 결정!
        for _ in range(len(dx)):
            nx = px + dx[_]
            ny = py + dy[_]
            # 만약, 격자안에 있고, 방문했고, step_map이 min_dist보다 작으면 최단거리니까 이동!
            if in_matrix_range(nx, ny) and visited_map[nx][ny] and step_map[nx][ny] < min_dist:
                min_cor_x = nx
                min_cor_y = ny
                min_dist = step_map[nx][ny]

        # 우선순위가 가장 높은 위치로 한 칸 이동!
        people[i] = [min_cor_x, min_cor_y]

    # step 2. 만약 편의점에 도착한다면 해당 편의점에서 멈추게 되고, 이때부터 다른 사람들은 해당 편의점이 있는 칸을 지나갈 수 없게 만들기
    for i in range(m):
        if people[i] == convenient[i]:
            px, py = people[i]
            board[px][py] = 2

    # step 3. 현재 시간이 t분이고 t ≤ m를 만족한다면, t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들어감

    # curr_t가 m보다 크다면 패스합니다.
    if current_time > m:
        return

    # Step 3-1. 편의점으로부터 가장 가까운 베이스 캠프를 고르기 위해
    #           편의점을 시작으로 하는 BFS를 진행합니다.
    bfs(convenient[current_time-1])

    # Step 3-2. 편의점에서 가장 가까운 베이스 캠프를 선택합니다.
    #           i, j가 증가하는 순으로 돌리기 때문에
    #           가장 가까운 베이스 캠프가 여러 가지여도
    #           알아서 (행, 열) 우선순위대로 골라집니다.
    min_dist = sys.maxsize
    min_cor_x = 0
    min_cor_y = 0

    for j in range(n):
        for k in range(n):
            # 베이스 캠프일 경우
            if step_map[j][k] < min_dist and visited_map[j][k] and board[j][k] == 1:
                min_dist = step_map[j][k]
                min_cor_x = j
                min_cor_y = k

    people[current_time-1] = [min_cor_x, min_cor_y]
    board[min_cor_x][min_cor_y] = 2

# 전부 편의점에 도착헀는지를 확인합니다.
def end():
    # 단 한 사람이라도
    # 편의점에 도착하지 못했다면
    # 아직 끝나지 않은 것입니다.
    for i in range(m):
        if people[i] != convenient[i]:
            return False

    # 전부 편의점에 도착했다면 끝입니다.
    return True

if __name__ == "__main__":

    # n = 격자 크기, m = 사람 수
    n, m = map(int, input().split())

    # 0 = 이동가능 길, 1 = 베이스 캠프, 2 = 이동 불가!
    board = [list(map(int, input().split())) for _ in range(n)]

    # 편의점 좌표 정보
    convenient = list()
    for i in range(m):
        x, y = map(int, input().split())
        # 편의점 좌표는 index 1부터 시작! 0부터 아니고!
        convenient.append([x - 1, y - 1])

    # 사람 이동 방향 ↑, ←, →, ↓ 북 서 동 남 우선순위
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    # 격자 크기
    max_row = len(board)
    max_col = len(board[0])

    # people 정보 저장
    # 바깥에 있을 경우 -1, -1 아니면, 격자 안으로 와서 people의 좌표 정보
    empty = [-1, -1]
    people = [empty] * m

    # 현재 시간 저장
    current_time = 0

    # 최단거리 결과 기록 2차원 배열
    step_map = [[0]*n for _ in range(n)]

    # 방문했는지에 대한 결과 기록 2차원 배열
    visited_map = [[False]*n for _ in range(n)]

    # 1분에 한번씩 시뮬레이션을 진행합니다.
    while True:
        current_time += 1
        simulation()
        # 전부 이동이 끝났다면 종료합니다.
        if end():
            break

    print(current_time)
