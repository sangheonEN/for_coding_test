# 같은 수 여러번 가능
# 고른 수열은 비내림차순
# 3 2 x
# 3 2 1 x 3 3 3 o

def dfs(start):

    if len(result) == M:
        print(" ".join(map(str, result)))

        return


    for i in range(start, N+1):
        result.append(i)
        dfs(i)
        result.pop()




if __name__ == "__main__":
    N, M = map(int, input().split())

    result = []

    visited = [False] * (N+1)

    dfs(1)