# # queue로 품
# from collections import deque
#
# def solution(arr):
#     answer = []
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
#     print('Hello Python')
#
#     # stack으로 append로 넣고 똑같은 값 있으면 바로 pop
#     new_arr = []
#     new_arr.append(arr[0])
#
#     queue = deque(arr)
#     N = len(arr)
#
#     for i in range(N+1):
#         if queue[0] == new_arr[-1]:
#             queue.popleft()
#         else:
#             new_arr.append(queue[0])
#     return new_arr
#
# a = solution([1,1,3,3,0,1,1])
#
# print(a)


# stack으로 푸는법
def solution2(arr):
    stack = [arr[0]]
    result = [arr[0]]

    for num in arr:
        curr = stack.pop()
        if curr != num:
            result.append(num)

        stack.append(num)
    return result

a = solution2([1,1,3,3,0,1,1])
print(a)

# def solution(arr):
#     stack = []
#     result = [arr[0]]
#     for num in arr:
#         if stack:
#             curr = stack.pop()
#             if curr != num:
#                 result.append(num)
#
#         stack.append(num)
#     return result
#
#
# # stack[]에 첫 수 넣고

# 리스트 슬라이싱으로 마지막부터 확인 a[-1:]
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print( no_continuous( "133303" ))

