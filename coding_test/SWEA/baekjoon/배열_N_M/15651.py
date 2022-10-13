# 1 -> 1, 2, 3, 4
# 2 -> 1, 2, 3, 4
# Tree 구조를 생각해보면서 해보자! 동일 숫자도 하니까 dfs(i+1)을 넣어주는게 아니라 1부터 다시 탐색하도록 dfs(1)로 재귀호출하여 탐색!
# 방문 check list도 사용하면 안됨! 1 1도 포함해야되서

def dfs(start):

    if len(result) == M:

        print(" ".join(map(str, result)))
        return

    for i in range(start, N+1):
        # if visited[i]:
            # continue
        result.append(i)
        # visited[i] = True
        dfs(1)
        result.pop()
        # visited[i] = False

if __name__ == "__main__":

    N, M = map(int, input().split())

    # visited = [False] * (N+1)

    result = []

    dfs(1)

