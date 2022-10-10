from collections import deque

global visited

def bfs(maps, visited, com):
    queue = deque()
    queue.append(com)
    visited[com] = True

    while queue:
        node = queue.popleft()
        for i in range(com):
            if maps[node][i] == 1 and visited[i] == False:
                visited[i] = True
                queue.append(i)


def solution(n, computers):
    visited = [False] * n
    count = 0

    for com in range(n):
        if visited[com] == False:
            bfs(computers, visited, com)
            count+=1

    return count

a = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])