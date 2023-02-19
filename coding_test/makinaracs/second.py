

def solution(P):

    def solve(start, cnt):
        elements = list(set(P))
        j = 0
        first = True

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

        return cnt

    cnt = 0
    visited = [False] * len(P)
    P.sort()

    for i in range(len(P)):
        if P[i] == min(P) and not visited[i]:
            cnt = solve(i, cnt)
            cnt += cnt

    if not all(visited) or cnt == 0:
        print(-1)
    else:
        pass
    return cnt

print(solution([3, 2, 1, 4, 5]))