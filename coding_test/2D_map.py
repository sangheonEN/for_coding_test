map = [
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1]
]

# print(map[행][열])
# 행은 가로줄, 열은 세로줄
# for 행 in range(len(map)):
#     for 열 in range(len(map)):
#         map[행][열] = 3
# print(map)

# max 격자칸 길이 확인
print(f"열의 길이 : {len(map[0])}")
print(f"행의 길이 : {len(map)}")

from collections import deque


def solutions(map):
    # 동서남북
    x_m = [0, 0, 1, -1]
    y_m = [1, -1, 0, 0]

    # 격자 칸 max, min 넘어가면 안되도록 제한하기
    x_max = len(map)
    y_max = len(map[0])

    def update(start_row, start_col, map):
        # 시작 점
        queue = deque([[start_row, start_col]])

        # queue에 들어간 데이터가 없어질때 까지 루프
        while queue:
            x, y = queue.popleft()
            # 4방향 서칭
            for i in range(4):
                nx = x + x_m[i]
                ny = y + y_m[i]

                # 격자 안에 들어왔을 제약 조건
                if nx > -1 and ny > -1 and nx < x_max and ny < y_max:
                    if map[nx][ny] == 0:
                        map[nx][ny] = 2

        return map

    for row in range(len(map)):
        for col in range(len(map[0])):
            map = update(row, col, map)

    print(map)

solutions(map)
