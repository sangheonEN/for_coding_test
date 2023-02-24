import heapq
import collections
from typing import List

"""
node, edge 정보 from, to, distance
1 2 3
1 3 4
2 1 3
2 4 2
3 2 1
3 4 1

start: 1, end: 4
"""

class Solution:
    def dijkstra_algorithm(self, node_info, start, end, N):

        graph = collections.defaultdict(list) # collections.defaultdict 순서가 있는 dict 변수 선언 가능

        for src, dst, dis in node_info:
            graph[src].append([dst, dis]) # graph[출발노드].append([도착노드, 거리])
            # defaultdict(<class 'list'>, {1: [[2, 3], [3, 4]], 2: [[1, 3], [4, 2]], 3: [[2, 1], [4, 1]]})

        queue = [[start, 0]] # (거리, 출발노드) 배열 초기화

        # node index별로 최단 distance 저장
        INF = int(1e9)

        dist = [INF] * (N+1)

        while queue:
            node, distance = heapq.heappop(queue)

            if dist[node] < distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
                continue

            # 현재 node의 distance 갱신
            dist[node] = distance

            # 인접 노드 탐방
            for next_node, next_distance in graph[node]:
                # 누적 거리를 저장
                cumulative_distance = distance + next_distance
                # 알고리즘을 반복할 때마다 실시간으로 시작노드와 가장 가까운 노드를 저장하기 위한 목적으로 우선순위 큐를 활용
                # 우선순위가 없는 큐 자료구조로 구현하면, 인접한 노드들 중에 가장 가까운 노드 찾기 위해 결국 전부 탐색해야되니 시간복잡도가 늘어난다.
                heapq.heappush(queue, [next_node, cumulative_distance])

        # target node까지의 최단 거리 출력
        return dist[end]

        # # m을 반복해서 max 값으로 갱신, dist[0] 인덱스에는 INF가 저장되어 있으니 해당 index는 제외하고 루프문 수행.
        # m = 0
        # for d in range(1, len(dist)):
        #     if INF <= dist[d]:
        #         return -1
        #     m = max(m, dist[d])
        # return m


if __name__ == "__main__":

    # graph 정보 입력 받기. 간선 수만큼 정보가 주어짐. [[from, to, distance], ...]

    edge = 6
    start = 1
    end = 4
    N = 4
    node_info = [list(map(int, input().split())) for _ in range(edge)]

    a = Solution()
    distance = a.dijkstra_algorithm(node_info, start, end, N)
    print(distance)



"""
import heapq
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    INF = int(1e9)

    graph = [[] for _ in range(n + 1)]

    for i in times:
        a, b, c = map(int, i)
        graph[a].append((b, c))

    def dijkstra_pq(graph, start):
        N = len(graph)
        dist = [INF] * N

        q = []
        heapq.heappush(q, (0, start))
        dist[start] = 0

        while q:
            acc, cur = heapq.heappop(q)

            if dist[cur] < acc:
                continue

            for adj, d in graph[cur]:
                cost = acc + d
                if cost < dist[adj]:
                    dist[adj] = cost
                    heapq.heappush(q, (cost, adj))

        return dist


    dist = dijkstra_pq(graph, k)
    m = 0
    for d in range(1, len(dist)):
        if INF <= dist[d]:
            return -1
        m = max(m, dist[d])
    return m
    

"""

