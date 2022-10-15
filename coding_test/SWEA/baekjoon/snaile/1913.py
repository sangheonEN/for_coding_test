# N, M이 주어지고 NXN 의 행렬이 주어지는데, M의 값이 어느 좌표에 있는지 출력하기.
# N X N은 달팽이 행렬 중앙픽셀부터 만들어짐

def in_range(x, y, N):
    return 0 <= x and x < N and 0 <= y and y < N


if __name__ == "__main__":

    N = int(input())
    M = int(input())

    snail_board = [[0]*N for i in range(N)]

    # 동 남 서 북 -> 동동동동남남남서서서서북북북북 이런식으로 달팽이 배열 만들기 때문에 저렇게 순서를 정해줌. 내가 원하는데로 정할 수 있음.
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cur_num = N ** 2
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

    for i in range(N):
        for j in range(N):
            if snail_board[i][j] == M:
                result_x = i
                result_y = j


    for row in snail_board:

        print(" ".join(map(str, row)))

    # for row in snail_board:
    #     print(*snail_board)
    print(result_x, result_y)
