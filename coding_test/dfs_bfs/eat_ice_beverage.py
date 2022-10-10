# N X M 사이즈의 얼음 틀이 있다. 구멍이 뚤린 부분은 0, 칸막이가 존재하는 부분은 1
# 상, 하, 좌, 우로 붙어 있는 경우 연결 된 노드
# 얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성해봐라
# 다음의 4 X 5 얼음 틀 예시는 총 3개 생성
# 1 <= N, M <= 1000 최대 100만개

def dfs(x, y):
    # map 벗어남 탈출
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:

        graph[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True
    return False


n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1


print(result)