# 6x6 판넬에서 1과 0으로 되어 있는 map이 형성된다.
# map에서 0이 인접해 붙어 있는 영역이 같은 영역이고 떨어져 있으면 다른 영역으로 본다.
# 최종적으로 구분되는 영역의 숫자를 return 하시오!

from collections import deque

map = [
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1]
]


def solutions(map):

    def update_panel(start, panel):
        max_x, max_y = len(panel) - 1, len(panel) - 1
        queue = deque([start])

        while len(queue) > 0:
            x, y = queue.popleft()
            # 북
            if y != 0 and panel[y - 1][x] == 0:
                queue.append([x, y-1])
            # 동
            if y != max_y and panel[y+1][x] == 0:
                queue.append([x, y+1])
            # 서
            if x != 0 and panel[y][x-1] == 0:
                queue.append([x-1, y])
            # 남
            if x != max_x and panel[y][x+1] == 0:
                queue.append([x+1, y])

            panel[y][x] = 2
        return panel

    answer = 0
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == 0:
                answer += 1
                map = update_panel([j, i], map)

    return answer


solutions(map)
