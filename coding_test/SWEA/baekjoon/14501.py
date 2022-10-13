# T 상담 시간, P 상담 비용
# N 퇴사날 N+1에 퇴사


def dp(N, T, P):

    dp = []

    for i in range(N):
        dp.append(P[i])

    dp.append(0)

    # 마지막은 어차피 수술을 못잡는다! dp 맨끝에 0을 넣는다.
    # 끝에서부터 순회해서 수술 시간 + 날짜를 더한게 N보다 크면 수술을 못하는 거니, dp[i]에 dp[i+1]을 저장한다. 끝에서부터 수술할 수 있을때까지 찾음
    # N보다 작으면 수술할 수 있는거니까, dp[i]에 dp[i + 1]과 p[i] + dp[i + t[i]]

    for i in range(N - 1, -1, -1):
        # print(i)
        # print(dp[i])
        if T[i] + i > N:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], P[i] + dp[i + T[i]])
    print(dp[0])

# DFS 풀이
# global answer 전역으로 해서 가장 높은 값만 저장해서 업데이트 시킴!
# 첫째날부터 N째날까지 순회하면서 비용을 계속산정함!
# 재귀함수 호출하는건 수술 날짜 + 수술에 드는 시간을 더한게 N보다 작거나 같으면 수술할 수 있는거니까 그날로 이동해서 수술하고 비용을 산정한다!
# 수술을 못할 경우 다음 날로 이동해서 다시 수술 계획을 짠다!


def dfs(day, p_total):
    global answer

    if day == N:
        answer = max(answer, p_total)
        return

    t_curr = T[day]
    p_curr = P[day]

    if t_curr + day <= N:
        dfs(t_curr + day, p_total + p_curr)
    dfs(day+1, p_total)


if __name__== "__main__":
    N = int(input())

    T = []
    P = []
    for i in range(N):
        t, p = map(int, input().split())
        T.append(t)
        P.append(p)

    dp(N, T, P)
    # answer = 0
    # p_total = 0
    #
    # for day in range(N):
    #     dfs(day, p_total)
    #
    # print(answer)