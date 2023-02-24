"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

"""


from typing import List
from collections import defaultdict
import heapq



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        # graph 정보 저장
        graph = defaultdict(list)

        for fr, to, pr in flights:
            graph[fr].append([to, pr])

        # 최소 price 정보 저장
        INF = int(1e9)
        price = [INF] * n

        # 출발 node 정보 저장, price, node, 경유수(횟수 0부터 시작)
        queue = [[0, src, 0]]

        # key는 node를 뜻하고, value는 방문 이전 경유 횟수를 뜻함.
        # 우선순위 큐로 cost가 최소인 경로를 추출해왔기 때문에 방문 이후 다른 경로에서 해당 노드를 재방문할때,
        # 해당 노드를 방문하기 이전의 경유 횟수 보다 더 적거나 같아야 한다.
        #
        """
        flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
        방문체크로 시간초과 문제 test case해결
        """
        visited = {}

        while queue:

            # 우선 순위 큐에서 가장 작은 가격 순으로 pop
            cur_price, cur_node, k = heapq.heappop(queue)

            # 뒤에 더 탐색할 노드가 있으면 탐색. 우선순위 queue로 앞의 node 탐색할때, k조건이 -1되어버려서 앞에서 stop됨.
            # 예외 test case [0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]
            if graph[cur_node]:
                pass

            else:
                if cur_price > price[cur_node]: # 새롭게 갱신할 dist가 더 크면 탐색 필요 없음. continue
                    continue

            # 현재 노드의 최소 경유 비용 업데이트.
            price[cur_node] = cur_price

            # 현재 node가 목적지 dst라면 탐색 종료.
            if cur_node == dst:
                return price[dst]

            # k는 최소 경유수, k = 0 이라면 직항!
            # 인접노드 탐색 전에 제약조건이 있음.
            # 현재 노드를 방문한적 없거나 방문했더라도, 경유 횟수가 방문 전의 경유 횟수가 더 크거나 같아야 탐색
            # 왜냐하면, 우선순위 queue로 인접한 node 중 가장 가까운 node를 찾았으니, 그것보다 더 경유 횟수가 작거나 같을 것이니까!
            # if cur_node not in visited or visited[cur_node] >= k:
            if cur_node not in visited or visited[cur_node] >= k:
                visited[cur_node] = k
                if k <= K:
                    # 인접노드 탐색
                    for next_node, next_price in graph[cur_node]:
                        # 인접한 노드로 갈때 드는 누적 비용 저장
                        cumulative_price = price[cur_node] + next_price
                        # 인접노드 정보 저장하는데 한번 경유했으니 k+1 처리.
                        heapq.heappush(queue, [cumulative_price, next_node, k+1])


        # 도착할 수 없으면 -1
        return -1



if __name__ == "__main__":
    n = 13
    flights = [[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]    # [[from, to, price], ...]
    src = 10
    dst = 1
    k = 10

    solving_code = Solution()
    result = solving_code.findCheapestPrice(n, flights, src, dst, k)
    print(result)

