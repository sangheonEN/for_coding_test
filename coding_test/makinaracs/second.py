def solution(P):

    def solve(start):
        elements = list(set(P))
        j = 0
        first = True
        nonlocal cnt
        nonlocal visited

        for i in range(start, len(P)):
            if P[i] == elements[j] and not visited[i]:
                visited[i] = True

                if P[i] == elements[-1]:

                    if first:
                        cnt += 1
                        first = False

                    j = 0
                    continue
                j += 1

    P.sort()
    visited = [False] * len(P)
    cnt = 0

    for i in range(len(P)):
        if P[i] == min(P) and not visited[i]:
            solve(i)

    if not all(visited) or cnt == 0:
        print(-1)
    else:
        pass

    return cnt



P = [3, 2, 1, 4, 5]
print(solution(P))