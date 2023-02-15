# https://inhyo.gitbook.io/algorithm-interview/13/40

from typing import List
import collections, heapq
from collections import deque


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """

        :param times: times: [u, v, w] 출발지, 도착지, 소요 시간 입력 list
        :param N: 전체 노드의 개수
        :param K: 출발 노드
        :return: K부터 출발해 모든 노드가 신호를 받을 수 있는 시간 리턴, 불가능할 경우 -1 리턴
        입력
        times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        출력
        2
        고찰: 다익스트라는 최단 거리를 구하는 것이기 때문에, 우선순위 heap을 사용한다.
             우선순위 heap: 새 요소가 힙에 추가되면 자동으로 재구성되어 순서를 유지한다.
             우선순위 큐를 최소 힙으로 구현하는 경우 가치가 낮은 데이터가 먼저 삭제되고
             최대 힙으로 구현하는 경우 가치가 높은 데이터가 먼저 삭제된다.
             그래서 deque를 활용한 queue구조는 node 상태를 update한 뒤에 또 최소, 최대에 따라 정렬을 해주는 작업이 필요하기 때문에 heapq 패키지를 이용한다.
        """
        graph = collections.defaultdict(list)

        for u, v, w in times:
            # graph[출발노드].append((도착노드, 소요시간))
            # graph = {출발노드 : [(도착노드, 소요시간)]} 저장됨. -> key는 출발노드, value는 [(도착노드, 소요시간)]
            # 출발노드가 중복되면 해당 출발노드 key의 value list에 append로 쌓인다.
            """graph는 전체 node들의 정보를 저장."""
            graph[u].append((v, w))

        # K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산
        # Q = [(time, node)] 시작 Node K 부터!
        # Q의 역할은 출발노드부터 완전 탐색을 시작하면서,
        # graph에 있는 다음 노드와 소요시간 데이터를 불러와 출발 노드부터 시작한 해당 노드까지의 소요 시간을 업데이트한다.
        Q = [(0, K)]
        # Q = deque([(0, K)])
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            # time, node = Q.popleft()
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    # 누적 소요시간을 저장한다.
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
                    # Q.append((alt, v))

        if len(dist) == N:
            return max(dist.values())

        return -1


if __name__ == "__main__":
    a = Solution()

    result = a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)

    print(result)


