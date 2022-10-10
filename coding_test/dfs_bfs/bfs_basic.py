# queue의 자료구조를 사용함
# 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 큐에서 노드를 꺼낸 뒤 해당 노드의 인접 노드 중에서 방문하지 않는 노드를 모두 큐에 삽입하고 방문 처리
# 2번 과정을 수행할 수 없을때까지 반복

from collections import deque

graph_1 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1,7]
]

visited = [False] * 9

def bfs(graph, start, visited):
    # 시작 노드를 queue에 넣는다.
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # queue에서 원소를 뽑고 방문하는 노드를 표현
        v = queue.popleft()
        print(v, end=" ")
        # 아직 방문하지 않은 인접한 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph_1, 1, visited)
