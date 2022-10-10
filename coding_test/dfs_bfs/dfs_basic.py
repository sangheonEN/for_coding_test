# 그래프를 그린다
# stack 자료구조를 사용함!
# 방문 기준: 번호가 낮은 인접 노드부터 방문
# 방문한 곳은 방문 x
# 가장 깊이 탐색 후 마지막 node 빼줌
# 재귀함수 사용 가능

# 1번 노드와 인접한 노드 정보 [2, 3, 8]
# 2번 노드와 인접한 노드 정보 [1, 7]
# 낮은 번호로 정렬되어 있어야 낮은 번호부터 방문 가능!
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

graph_2 = [
    [],
    [2, 3],
    [4, 5],
    [6],
    [2],
    [2],
    [3]
]

# 각 노드가 방문된 정보를 표현 초기 값 False로 node+1 수 만큼 일차원 데이터
visited_1 = [False] * 9
visited_2 = [False] * 7

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    # 낮은 번호의 인접한 노드부터 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph_2, 1, visited_2)









