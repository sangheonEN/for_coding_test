from itertools import permutations

def dfs():

    # 종료 조건 result[]에 저장되는 원소가 2개 되면 출력
    if len(result) == M:
        # print(" ".join(map(str, result)))
        return

    for i in range(1, N+1):
        if visited[i]:
            continue

        visited[i] = True

        result.append(i)
        print(result)
        dfs()
        result.pop()
        visited[i] = False


def iter_tools():
    import itertools
    nums = [i for i in range(1, N+1)]
    array = itertools.permutations(nums, M)

    for i in array:
        for j in i:
            print(j, end=" ")
        print()

if __name__ == "__main__":


    N, M = map(int, input().split())

    result = []

    visited = [False]*(N+1)

    # dfs()

    iter_tools()
