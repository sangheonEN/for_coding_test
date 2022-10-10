# 최단 거리 계산
# 매번 새로운 지점을 방문할때 첫 시작점부터의 거리를 출력해보자!

from collections import deque
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 4 방향 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 0 ~ n-1, 0 ~ m-1 map 형성
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 0인 지점은 방문 x
            if graph[nx][ny] == 0:
                continue
            # 1인 지점을 방문하고 이전 지점의 값에 + 1을 저장
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))



