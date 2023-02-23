
"""
일반적으로 최단, 최소를 구할때 사용함.
특히, 다익스트라는 최단, 최대 거리를 구하는 문제에 사용함.
      1. 우선순위 heap: 새 요소가 힙에 추가되면 자동으로 재구성되어 순서를 유지한다.
      2. 우선순위 큐를 최소 힙으로 구현하는 경우 가치가 낮은 데이터가 먼저 삭제되고
      3. 최대 힙으로 구현하는 경우 가치가 높은 데이터가 먼저 삭제된다.
      4. 그래서 deque를 활용한 queue구조는 node 상태를 update한 뒤에 또 최소, 최대에 따라 정렬을 해주는 작업이 필요하기 때문에 heapq 패키지를 이용한다.
"""

#%%
import heapq

# heappush를 할때마다, 새 요소가 힙에 추가되면서 자동으로 최소 힙으로 재구성되어 순서를 유지한다.
# 1. 최소 우선 순위 힙 구조
Q = []
heapq.heappush(Q, 5)
heapq.heappush(Q, 4)
heapq.heappush(Q, 10)
heapq.heappush(Q, 2)
print(Q)
heapq.heappop(Q)
print(Q)


#%%
import heapq

# 2. 최대 우선 순회 힙 구조
num = [5, 2, 3, 2, 10, 1]
heap = []
max_heap = []

# 0 index에 n의 음수 값을 저장해서, 가장 낮은 수가 큰 값으로 우선 순위되도록 힙 정렬을 함.
for n in num:
    heapq.heappush(heap, (-n, n))

print(heapq)

while heap:
    max_heap.append(heapq.heappop(heap)[-1])

print(max_heap)

#%%
import heapq

# 3. 이미 원소가 있는 list를 heap으로 바꾸기
Q2 = [4, 2, 1, 2, 10]
heapq.heapify(Q2)

print(Q2)

#%%
import heapq

# 4. n번째 최소값 or 최대값 출력
Q4 = [4, 2, 1, 2, 10]
n = 2
def nth_smallest(arr, n):
    heap = []
    for num in arr:
        # 최소 우선 순위 힙으로 정렬됨.
        heapq.heappush(heap, num)

    nth_min = None

    for _ in range(n):
        # stack 구조로 최소 값이 저장된 첫순서부터 n번 순서까지 pop.
        nth_min = heapq.heappop(heap)

    return nth_min

def nth_biggest(arr, n):
    heap = []
    for num in arr:
        heapq.heappush(heap, (-num, num))

    nth_max = None

    for _ in range(n):
        nth_max = heapq.heappop(heap)[-1]

    return nth_max

print(nth_smallest(Q4, n))
print(nth_biggest(Q4, n))


