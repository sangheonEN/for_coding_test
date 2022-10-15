# 2차원 정방행렬에 대한 값을 회전해보자!

def rotated(a):
    # 새로운 result 0의 원소를 가진 2차원 빈리스트 생성
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    # n, m 만큼 반복하면서 result update
    # 세로로 수행
    # result[j]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


# 시계방향 90도 rotation
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
            new_board[rx + sx][ry + sy] = arr[x][y]


# 반시계방향 90도 rotation
def not_clock_rotate_square(sx, sy, square_n):
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
            new_board[ry + sy][rx + sx] = arr[y][x]


# horizontal 좌우 측면 바꾸기
def left_right_change(sx, sy, square_n):
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
            new_board[rx + sx][ry + sy] = arr[y][x]


# 상측 하측 면 바꾸기 vertical flip
def top_bottom(sx, sy, square_n):
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
            new_board[ry + sy][rx + sx] = arr[x][y]


if __name__ == "__main__":

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    b90 = rotated(arr)
    c180 = rotated(b90)
    d270 = rotated(c180)
    # print(arr)
    # print(b90)
    # print(c180)
    # print(d270)

    new_board = [[0] * M for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         new_board[i][j] = 0
    move_num = N
    not_clock_rotate_square(0, 0, move_num)
    print(new_board)


