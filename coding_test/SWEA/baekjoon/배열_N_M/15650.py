# N, M 길이가 M인 수열 구하기
# 오름차순
# 중복없이 -> 순서 상관 X
# 조합 문제!


def dfs(start):

    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(start, N+1):

        if visited[i]:
            continue

        if i not in result:
            visited[i] = True
            result.append(i)
            dfs(i+1)
            visited[i] = False
            result.pop()

if __name__ == "__main__":

    N, M = map(int, input().split())

    result = []

    visited = [False] * (N+1)

    dfs(1)
