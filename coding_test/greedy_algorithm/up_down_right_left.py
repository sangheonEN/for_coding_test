# N X N 크기의 정사각형 공간 위에 서 있다.
# 가장 위 왼쪽 좌표 (1, 1), 가장 아래 오른 좌표 (N, N)
# L, R, U, D -> Left, Right, Up, Down
# 1 <= N <= 100, 1 <= 이동 횟수 <= 100
# Map을 벗어나는 행동은 하지 않는다.

N = 5
move = "R R R U D D"
# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move_types = ['R', 'L', 'D', 'U']


x, y = 1, 1

for m in move:
    if m == " ":
        continue

    # 좌표 이동 move type에 따라
    for i in range(len(move_types)):
        if m == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # map 벗어남 방지
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x = nx
    y = ny

print(x, y)
