"""
n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

입출력 예
numbers	         target  return
[1, 1, 1, 1, 1]	  3	        5
[4, 1, 2, 1]	  4	        2

"""

# +, -를 주어진 numbers에 다 적용해보고 나온 결과 값이랑 target이랑 같으면 return count += 1을 주는 식으로 구현해보자.

# from collections import deque
#
#
# # popleft() 는 idx도 반환한다.
#
# def bfs(graph, target):
#     answer = 0
#     queue = deque()
#     queue.append([graph[0], 0])
#     queue.append([-1*graph[0], 0])
#
#     while queue:
#         temp, idx = queue.popleft()
#
#         idx += 1
#
#         if idx < len(graph):
#             queue.append([temp + graph[idx], idx])
#             queue.append([temp - graph[idx], idx])
#             print(queue)
#         else:
#             print(queue)
#             if temp == target:
#                 answer += 1
#
#     return answer
#
#
# def solution(numbers, target):
#
#
#     result = bfs(numbers, target)
#
#
#     return result
#
#
# result = solution([1, 1, 1, 1, 1], 3)
# print(result)




from itertools import product

def b(a, c, d, e, f):
    print(a)
    print(c)
    print(d)
    print(e)
    print(f)

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    b(*l)
    s = list(map(sum, product(*l)))
    return s.count(target)

result = solution([1, 1, 1, 1, 1], 3)
print(result)

print(list(map(sum,product([1, -1], [1, -1], [1, -1], [1, -1], [1, -1]))))