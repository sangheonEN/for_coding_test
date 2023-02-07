# 자료구조는 graph를 사용
# node와 가중치를 가진 간선을 이용해 실제 거리를 표현
# 방문하지 않은 인접 노드를 방문할때, 현재까지 발견된 가장 짧은 거라의 노드에 대해 먼저 계산할 수 있으며,
# 더 긴 거리로 계산 되었을 시 스킵 또한 가능함.
# 우선순위 heap을 알아야한다!
import heapq

h = []
# heappust(list_arr, 삽입 원소)
heapq.heappush(h, 3)
print(h)

# heap sort
h = [3, 9, 1, 4, 2]
heapq.heapify(h)

for _ in range(len(h)):
    print(heapq.heappop(h))