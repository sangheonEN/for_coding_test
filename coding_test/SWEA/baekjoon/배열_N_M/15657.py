# 비내림차순을 위해서!
# result에 뭐라도 있으면 elif로 넘어가서 지금 가지고 있는 첫번째 원소와 다음 뎁스의 i번째 원소들을 다 비교하면서 i번째 원소가 클 경우만 append!


def dfs(start):

    if len(result) == M:
        print(" ".join(map(str, result)))
        # result_list.append(result[:])
        return

    for i in range(start, len(input_list)):

        # if visited[i] == True:
        #     continue
        # visited[i] = True
        # result에 뭐라도 있으면 elif로 넘어가서 지금 가지고 있는 첫번째 원소와 다음 뎁스의 i번째 원소들을 다 비교하면서 i번째 원소가 클 경우만 append!
        if not result:
            result.append(input_list[i])
            dfs(start)
            result.pop()
        elif result[-1] <= input_list[i]:
            result.append(input_list[i])
            dfs(start)
            result.pop()
        # visited[i] = False


if __name__ == "__main__":

    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    # print(N, M)
    # print(input_list)

    input_list.sort()

    result = []
    result_list = []

    visited = [False] * N

    dfs(0)

    # print(result_list)