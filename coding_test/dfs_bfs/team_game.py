from collections import deque


# def dfs(maps, x, y, count, visited):
#     # 동 서 남 북
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     for step_idx in range(len(dx)):
#
#         if x == len(maps[0])-1 and y == len(maps[1])-1:
#             return count
#
#         nx = x + dx[step_idx]
#         ny = y + dy[step_idx]
#
#         if nx < 0 or ny < 0 or nx > len(maps[0])-1 or ny > len(maps[1])-1:
#             continue
#
#         if maps[nx][ny] == 1 and visited[nx][ny] == False:
#             count += 1
#             visited[nx][ny] = True
#             dfs(maps, nx, ny, count, visited)
#
#     return -1

# def solution(maps):
#     x, y = 0, 0
#
#     count = 1
#
#     visited = [[False] * len(maps[0]) for _ in range(len(maps[1]))]
#
#     answer = dfs(maps, x, y, count, visited)
#
#     return answer
#
# a = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
#
# print(a)

# def bfs(maps, x, y):
#     # 동 서 남 북
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]
#
#     queue = deque()
#     queue.append((x, y))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for step_idx in range(len(dx)):
#
#             nx = x + dx[step_idx]
#             ny = y + dy[step_idx]
#
#             if nx < 0 or ny < 0 or nx > len(maps[0])-1 or ny > len(maps[1])-1:
#                 continue
#
#             if maps[nx][ny] == 1:
#                 maps[nx][ny] = maps[x][y]+1
#                 queue.append((nx, ny))
#
#             elif maps[nx][ny] == 0:
#                 continue
#
#             else:
#                 pass
#
#     return maps[len(maps[1])-1][len(maps[0])-1] if maps[len(maps[1])-1][len(maps[0])-1] > 1 else -1
#
#
#
#
# def solution(maps):
#     x, y = 0, 0
#
#     print(len(maps))
#
#     answer = bfs(maps, x, y)
#
#     return answer

# a = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
#
# print(a)



"""
다른사람이 짠거 내꺼랑 비교하면 deque([0, 0, 1]) x, y, count를 넣어서 사용함.
"""
from collections import deque

def solution(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])


    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1


a = solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])

print(a)