# 4 2
# 9 7 9 1
# 1 7
# 1 9
# 7 1
# 7 9
# 9 1
# 9 7
# 9 9
# 중복 수열 ㄴㄴ -> set,

def dfs(start):
    overlap = 0

    if len(result) == M:
        # if result in result_list:
        #     return
        # result_list.append(result[:])
        print(" ".join(map(str, result)))
        return

    # start + 1 하면서 for문을 한단계씩 늘리면 중복되는게 없어짐.
    for i in range(start, len(input_list)):

        if visited[i]:
            continue

        if overlap != input_list[i]:

            if not result:
                #visited의 역할은 다 return되고 난 후에 맨 처음 뎁스에서 이전에 방문한 노드는 방문하지 않도록 한다.
                visited[i] = True
                result.append(input_list[i])
                overlap = input_list[i]
                # start + 1과 start의 차이, start+1은 계속 i가 1증가하므로 다음 뎁스에서 자기 자신을 탐색하지 않는다.
                dfs(start+1)
                result.pop()
                visited[i] = False
            elif result[-1] <= input_list[i]:
                #visited의 역할은 다 return되고 난 후에 맨 처음 뎁스에서 이전에 방문한 노드는 방문하지 않도록 한다.
                visited[i] = True
                result.append(input_list[i])
                overlap = input_list[i]
                # start + 1과 start의 차이, start+1은 계속 i가 1증가하므로 다음 뎁스에서 자기 자신을 탐색하지 않는다.
                dfs(start+1)
                result.pop()
                visited[i] = False


if __name__ == "__main__":

    N, M = map(int, input().split())

    input_list = list(map(int, input().split()))
    input_list.sort()
    result = []
    result_list = []
    # visited 방문 적용을 안하면 자기자신도 돌아버림
    visited = [False] * N

    dfs(0)
