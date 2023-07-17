# 격자 넘어간건지 아닌지 판별 함수
def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N


# 격자 안나갔고, 이전에 방문하지 않았고, 탐색 실시 다음 이동 board의 좌표 원소 값이 현재랑 같으면 이동!
def dfs(x, y):
    for i in range(len(dx)):
        nx = dx[i] + x
        ny = dy[i] + y

        if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] == board[x][y]:
            visited[nx][ny] = True
            group[nx][ny] = group_n
            group_cnt[group_n] += 1
            dfs(nx, ny)


def rotate_square(sx, sy, square_n):
    # 정사각형 시계방향으로 90도 회전
    # sx, sy 는 정사각형의 첫항 시작점!
    # square_n은 뭐지?
    for x in range(sx, sx+square_n):
        for y in range(sy, sy+square_n):
            # 정사각형 탐색 시작점을 sx, sy를 0, 0으로 변환 전체 사각형을 일반화 연산을 위해서 3, 3에 시작하는 정사각형도 0, 0 으로 이동한 뒤 한 칸씩 이동하면서 저장시킴
            ox, oy = x - sx, y - sy
            # ox, oy로 다음 좌표 회전한 rx, ry를 구하기
            # square_n - ox -1 이 가지는 의미가 x가 늘어날때마다 ox는 올라감 그래서 전체에서 - ox -1를 해주면 상단으로 이동하지!
            # oy를 그냥 해주는 이유는 y가 증가하면 oy가 1씩 높아지므로 변화되는 x는 우측으로 이동해야되서 사실 변화가 없음.
            rx, ry = oy, square_n - ox - 1
            # sx, sy가 3, 3이면 3, 4로 넣어주기 위해 sx, sy를 rx, ry에 더한 좌표로 next arr에 넣어주기
            next_board[rx + sx][ry + sy] = board[x][y]


# 회전은 무조건 next_board를 초기화하여 그 안에 원소를 기존 board의 값을 참조해서 입력하여 새롭게 만들자!!
def rotate():
    # 십자가 반시계 방향으로 회전 next board 초기화!
    for i in range(N):
        for j in range(N):
            next_board[i][j] = 0

    # 회전 시작!
    # 십자가 부터 회전
    for i in range(N):
        for j in range(N):
            # 만약 j == N // 2 라면! i를 기준으로 순회한 값 사용가능 그러니까, nextboard[j][i]로 해서 행을 고정하고 기존의 board[i][j] 행의 값을 넣어줌.
            #  1
            #  2 -> 1 2 3 이렇게 들어가게
            #  3
            if j == N//2:
                next_board[j][i] = board[i][j]
            #           3
            # 1 2 3 ->  2 이렇게 들어가게!
            #           1
            elif i == N//2:
                next_board[N-j-1][i] = board[i][j]

    # 나머지 정사각형 rotate
    square_n = N // 2
    rotate_square(0, 0, sqaure_n)
    rotate_square(0, sqaure_n + 1, sqaure_n)
    rotate_square(sqaure_n + 1, 0, sqaure_n)
    rotate_square(sqaure_n + 1, sqaure_n + 1, sqaure_n)


# 변수 선언 입력

if __name__ == "__main__":
    N = int(input())

    board = [list(map(int, input().split())) for i in range(N)]

    print(N)
    print(board)

    # 새로운 보드를 생성
    next_board = [[0]*N for _ in range(N)]

    # 그룹의 개수를 관리
    group_n = 0

    # 각 칸에 그룹 번호를 적어줌
    group = [[0] * N for _ in range(N)]

    # 각 그룹마다 칸의 수를 세어줌
    group_cnt = [0] * (N * N + 1)

    visited = [[False] * N for _ in range(N)]

    # 동 서 남 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]









