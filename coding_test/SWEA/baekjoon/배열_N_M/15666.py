# 4 2
# 9 7 9 1
# 1 7
# 1 9
# 7 1
# 7 9
# 9 1
# 9 7
# 9 9
# 같은 수는 선택 가능(visited배열안씀), 중복 되서 나타내면 안되(overlab사용),
# 오름차순으로 정렬([1, 2] 1번을 결정하는 뎁스의 원소 값과 2번을 결정하는 뎁스의 원소 값을 비교해서 2번이 클 경우만 append)!
"""
와 N과 M을 풀면서 얻은게
1. dfs 재귀적 트리 탐색 구조 -> 1번 문제부터 쭉 풀면 느낌이 온다. 그리고 디버그 열심히 해보기
2. overlab이 있을 경우 탐색에 포함 안하는 방법 -> 15664, 15665, 15666 문제 보기! 1 7 9 9 에서 9, 9가 한번만 나오고 또 안나오게!
3. visited 배열로 다음 원소를 탐색할때 그전에 탐색한 원소는 방문하지 않는 방법 -> 예를들어 1 7 9 9가 있을때 1, 1 - 7, 7 이런게 안나오게 (같은 수 반복 방지) 9, 9는 두개니까 나옴
4. sort
5. 내림 차순, 오름 차순으로 정렬하는 것 (탐색할때마다 이전 뎁스의 원소 값과 탐색 중인 현재 원소와 비교해서 현재 원소가 큰 경우 append하면 오름차순, 현재 원소가 작은 경우 append하면 내림차순)
6. 탐색 for i in range(start, N): 문에서 dfs 재귀할때 dfs(start+1)씩해주면 첫 번째 뎁스에서 중복 되는거 안 먹힘. 1 7 9 9에서 1 1이 안나옴 -> 15656 한번 더 보면 이해될듯
"""


def dfs(start):
    overlab = 0

    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(start, len(input_list)):

        if overlab != input_list[i]:
            overlab = input_list[i]
            if not result:
                result.append(input_list[i])
                dfs(start)
                result.pop()
            elif result[-1] <= input_list[i]:
                result.append(input_list[i])
                dfs(start)
                result.pop()

# def dfs(start):
#     overlap = 0
#
#     if len(result) == M:
#         # if result in result_list:
#         #     return
#         # result_list.append(result[:])
#         print(" ".join(map(str, result)))
#         return
#
#     # start + 1 하면서 for문을 한단계씩 늘리면 중복되는게 없어짐.
#     for i in range(start, len(input_list)):
#
#         if overlap != input_list[i]:
#
#             #visited의 역할은 다 return되고 난 후에 맨 처음 뎁스에서 이전에 방문한 노드는 방문하지 않도록 한다.
#             result.append(input_list[i])
#             overlap = input_list[i]
#             # start + 1과 start의 차이, start+1은 계속 i가 1증가하므로 다음 뎁스에서 자기 자신을 탐색하지 않는다.
#             dfs(start)
#             result.pop()


if __name__ == "__main__":

    N, M = map(int, input().split())

    input_list = list(map(int, input().split()))
    input_list.sort()
    result = []
    result_list = []
    # visited 방문 적용을 안하면 자기자신도 돌아버림
    # visited = [False] * N

    dfs(0)
