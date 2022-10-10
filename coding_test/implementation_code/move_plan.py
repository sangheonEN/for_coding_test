# n x n map에서 plan을 준다 R R R U D D -> 동 동 동 북 남 남 1, 1에서 시작해서 도착지점의 좌표 출력!
n = int(input())
plans = input().split()

# 시작 좌표
x, y = 1, 1

# 움직이는 방향 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
move_types = ['R', 'L', 'D', 'U']

# 탐색 시작!
# for plan in plans:
#     if plan in move_types:
#         if plan == 'R':
#             nx = x + dx[0]
#             ny = y + dy[0]
#         elif plan == 'L':
#             nx = x + dx[1]
#             ny = y + dy[1]
#
#         elif plan == 'D':
#             nx = x + dx[2]
#             ny = y + dy[2]
#         else:
#             nx = x + dx[3]
#             ny = y + dy[3]
#
#     if nx < 1 or nx > n or ny < 1 or ny > n:
#         continue
#
#     x = nx
#     y = ny
# print(x, y)

# 탐색 두번째 방법 if문 말고! for문으로 전체 MOVE TYPES 탐색하기.

for plan in plans:
    for move_idx in range(len(move_types)):
        if plan == move_types[move_idx]:
            nx = x + dx[move_idx]
            ny = y + dy[move_idx]

    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue

    x = nx
    y = ny

print(x, y)




