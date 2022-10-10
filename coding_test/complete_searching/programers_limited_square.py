from itertools import permutations

a = [[2, 3], [3, 4]]
c = [[2, 3]]

start = []
for i in a:
    start += i
print(start)

"""
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> start = []
>>> for i in a:
...     start += i
... 
>>> start
[1, 2, 3, 4, 5, 6]

"""
#
# def solution(sizes):
#     right = list()
#     left = list()
#
#     for i in range(len(sizes)):
#         right.append(sizes[i][0])
#         left.append(sizes[i][1])
#
#     right_max_idx = right.index(max(right))
#     left_max_idx = left.index(max(left))
#     temp = 0
#     if right[right_max_idx] > left[left_max_idx]:
#         temp = left[left_max_idx]
#         left[left_max_idx] = right[left_max_idx]
#         right[left_max_idx] = temp
#     elif right[right_max_idx] < left[left_max_idx]:
#         temp = right[right_max_idx]
#         right[right_max_idx] = left[right_max_idx]
#         left[right_max_idx] = temp
#     else:
#         pass
#
#     answer = max(right) * max(left)
#     return answer