from collections import deque

# queue에 1 2 3 2 3 1 0 담아 두고 하나씩 빼면서 price 각각 마다 비교해서 count 세기
# price: (1) 2 3 2 3 1 0
# queue: 2 3 2 3 1 0
# price 1부터 queue 하나씩 비교해가면서 price 이상이면, count하고 popleft로 빼버림.

def solution(prices):
    queue = deque(prices)
    result = []

    for i in range(len(prices)):
        count = 0
        queue.popleft()

        for q in queue:

            if q >= prices[i]:
                count += 1
            else:
                # price가 1일때 [1 2 3 2 3 1 0]
                # 0번을 만나면, count 한번 더 해주고 바로 탈출 해야 시간복잡도 줄임!
                count += 1
                break

        result.append(count)

    return result


# 다른 사람 풀이
# 내가 원하던 것이다. for문을 prices 수만큼하고, 이중 for문으로 i+1부터 탐색하도록 구현했다.

# def solution(prices):
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
#     return answer
