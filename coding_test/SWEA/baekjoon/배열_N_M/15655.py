
def dfs(start):

    if len(result) == M:
        print(" ".join(map(str, result)))

        return

    for i in range(len(input_list)):

        if visited[i]:
            continue
        visited[i] = True
        result.append(input_list[i])
        dfs(i+1)
        result.pop()
        visited[i] = False



if __name__ == "__main__":
    N, M = map(int, input().split())

    input_list = [i for i in map(int, input().split())]

    input_list.sort()

    # print(input_list)

    result = []

    visited = [False] * (N+1)

    dfs(0)