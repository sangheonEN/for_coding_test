"""
입력 n1에서 n2로 갈때 거리 distance(1, 2)
 [[n1, n2, distance(1, 2)],
  [n2, n3, distance(2, 3)],
  [n3, n4, distance(3, 4)],
  ...]

1 2 3
1 3 2
1 4 1
3 4 5
2 5 2
3 5 2
4 5 3

각 노드에서 다른 노드까지 최단 거리로 갈 수 있는 arr를 만들고
해당 노드를 선택하면 다른 노드까지 가는 최단 거리를 출력한다. 만약, 갈 수 없다면, inf를 출력

                     도착노드
        ________________________________
출발노드 |  1      2      3      4      5
        |________________________________
1번 출발 | inf     3      2      1      4
2번 출발 | inf    inf    inf    inf     2
3번 출발 | inf    inf    inf     5      2
...
...
"""


def dijkstra(node_idx):
    # 시작 노드에 대해서 초기화
    distance[node_idx] = 0
    visited[node_idx] = True

    for j in graph[node_idx]:
        distance[j[0]] = j[1]

    










if __name__ == "__main__":
    # 최단 거리 구할때 쓸려는 기준
    inf =1e8
    # graph 자료구조 list로 표현
    n = 5
    m = 7
    # 노드 연결 정보
    graph = [[] for i in range(n+1)]
    # 노드 방문 체크
    visited = [False] * (n + 1)
    # 최단 거리 정보보distance = [1e8] * n
    distance = [inf] * (n + 1)
    # result arr
    result = [[0] * n for i in range(n + 1)]

    # 모든 간선 정보 입력 받기
    for _ in range(m):
        # a -> b node로 이동할때 c거리 만큼 걸림
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # 1번 index에 저장된 원소는 graph[1] = 연결node, 거리
    # [[], [(2, 3), (3, 2), (4, 1)], [(5, 2)], [(4, 5), (5, 2)], [(5, 3)], []]
    print(f"graph : {graph}")
    print(f"visitaed : {visited}")
    print(f"distance : {distance}")
    print("--")

    # 다익스트라 알고리즘 수행
    start = 0
    for i in range(1, n + 1):
        dijkstra(i)
