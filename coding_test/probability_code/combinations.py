#backtracking
from collections import deque

def comb(start):
    # 종료조건: r만큼 result에 차면 result list에 append하고 return
    if len(result) == r:
        result_list.append(result)
        for i in range(len(result)):
            result.pop()
        return result_list

    for i in range(start, len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        result.append(arr[i])
        comb(i+1)
        # visited[i] = False



# def print(start, end):
#   for i in range(start+1, end):
#     print('['+arr[start]+','+arr[i]+']')
#   print(start+1, end)

arr = []

for i in range(3):
    for j in range(3):
       arr.append([i, j])

# arr에 [[0,0]~[n,n]]으로 생성
# 내가 원하는 출력 r = 2일때 [[0, 0], [1, 2]] 이런식으로 2개 뽑는 모든 경우의 수
visited = [False]*(len(arr))
r = 2
result_list = []
result = []
result_list = comb(0)
print(result_list)

