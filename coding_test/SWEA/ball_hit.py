# python은 새로 만들어 주면서 해보자!!
# 함수를 전역으로 사용할지 지역으로 사용할지 명확히 판단해야함.
# 함수를 가지고 계속 돌려 쓸거면 전역 아니면 지역으로! return하도록해서 사용

def in_range(x, y, N):
    return 0 <= x and x < N and 0 <= y and y < N


def snail_arr(snail_board):
    # 동 남 서 북 -> 동동동동남남남서서서서북북북북 이런식으로 달팽이 배열 만들기 때문에 저렇게 순서를 정해줌. 내가 원하는데로 정할 수 있음.
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cur_num = (N ** 2) -1
    cur_x, cur_y = 0, 0
    direction = 0

    result_x = 0
    result_y = 0

    # cur_num 1보다 작아지면 종료!
    while cur_num > 1:

        snail_board[cur_x][cur_y] = cur_num

        ny = dy[direction] + cur_y
        nx = dx[direction] + cur_x

        if in_range(nx, ny, N) and snail_board[nx][ny] == 0:
            cur_x = nx
            cur_y = ny
            cur_num -= 1
        # 다음 이동이 격자 바깥으로 나간다면, 방향 전환! 동 남 서 북
        else:
            direction = (direction + 1) % 4

    snail_board[cur_x][cur_y] = cur_num

    return snail_board

    # debug
    # for i in range(N):
    #     for j in range(N):
    #         if snail_board[i][j] == M:
    #             result_x = i
    #             result_y = j
    #
    #
    # for row in snail_board:
    #
    #     print(" ".join(map(str, row)))
    #
    # # for row in snail_board:
    # #     print(*snail_board)
    # print(result_x, result_y)

def arrtoarr2():

    for i in range(N**2):
        input_snail_board[position_arr[i][0]][position_arr[i][1]] = arr[i]


def arr2toarr():

    for i in range(N**2):
        arr[i] = input_snail_board[position_arr[i][0]][position_arr[i][1]]


def move():
    # 1차원 배열의 0의 원소를 사라지게함
    # temp는 arr에 있는 값을 저장함
    temp = [[0]* len(arr)]
    # 0이 나오면 건너 뛰도록! idx 써줌
    idx = 0

    for i in range(N**2):
        while (idx < (N**2) and arr[idx] == 0):
            idx += 1

        temp[i] = arr[idx]
        idx += 1

    for i in range(N**2):
        arr[i] = temp[i]


def break_f(a, b):
    # a방향에 따라 b만큼의 칸의 원소를 0으로 만듬

    # # 1 2 3 4 로 주어지니까 -1로 해서 빼주기
    # a -= 1

    # 방망이 위치
    start_x = N // 2
    start_y = N // 2

    # a는 위치 이동 방향 상, 하, 좌, 우 a는 1, 2, 3, 4로 주어짐 0은 없음 그래서 0번째 인덱스는 그냥 이동 방향 없음
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    # b칸 만큼 부숨
    for i in range(b):
        start_x = start_x + dx[a]
        start_y = start_y + dy[a]

        input_snail_board[start_x][start_y] = 0


def print_f():
    print(f"arr: {arr}")
    print(f"input_snail_board: {input_snail_board}")

if __name__ == "__main__":

    # 달팽이 배열로 index를 활용해서 일차원 배열로 변환하는 방법!
    # 일차원 배열로 변환한 뒤 달팽이

    N, M = map(int, input().split())

    snail_board = [[0]*N for i in range(N)]
    input_snail_board = [list(map(int, input().split())) for i in range(N)]
    # a 방향 1 상 2 하 3 좌 4 우 b 칸 만큼 내려침
    a, b = map(int, input().split())

    # index 사용할라고 임의로 생성함
    new_snail_board = snail_arr(snail_board)

    position_arr = [[0] * 2 for i in range(N**2)]

    arr = [0]*(N**2)

    # print(new_snail_board)

    # position arr에 N X N으로 시작되는 첫 시작점 5 X 5라면 24 23 22 21 20 ... 각 지점의 달팽이 원소의 좌표 값을 저장함
    # 각 지점의 임의로 내가 만들어 놓은 25 번째 달팽이 배열에 들어가는것을 0, 0으로 저장함
    for i in range(N):
        for j in range(N):
            position_arr[new_snail_board[i][j]][0] = i
            position_arr[new_snail_board[i][j]][1] = j

    # print(position_arr)
    #
    # 달팽이 배열 순서대로 arr 2차원에서 1차원 변환
    arr2toarr()
    # 1차원 배열에서 2차원 배열로 변환
    arrtoarr2()
    # print(arr2)

    print_f()
    break_f(a, b)
    arr2toarr()
    arrtoarr2()
    print_f()
    move()
    arrtoarr2()
    print_f()


    #
    # print(arr)
    # print(arr2)

    # print(input_snail_board)
    # break_f(a, b)
    # print(input_snail_board)

    # for _ in range(M):
    #     print(input_snail_board)
    #     break_f(a, b)
    #     print(input_snail_board)
        # move()
        # while bomb():
        #     move()
        # split()