# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 8방향


# 동쪽으로 한칸 이동!
x, y = 2, 2

nx = x + dx[0]
ny = y + dy[0]

# 동쪽으로 두칸 이동!
nx = x + 2*dx[0]
nx = y + 2*dy[0]

# 2차원 map 그리기 가로 n, 세로 m
n, m = 5, 5
map_1 = [[0]*n for _ in range(m)]
print(map_1)

