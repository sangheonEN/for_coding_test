# https://inhyo.gitbook.io/algorithm-interview/13/40

from typing import List
import collections, heapq
from collections import deque


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산
        # Q = [(time, node)] 시작 Node K 부터!
        Q = deque([(0, K)])
        dist = collections.defaultdict(int)

        while Q:
            # time, node = heapq.heappop(Q)
            time, node = Q.popleft()
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    # heapq.heappush(Q, (alt, v))
                    Q.append((alt, v))
        if len(dist) == N:
            return max(dist.values())

        return -1


if __name__ == "__main__":
    a = Solution()

    result = a.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)

    print(result)


