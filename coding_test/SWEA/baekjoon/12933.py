# 풀이법
# 1. "quack" 이라는 문자열을 선언하고, 입력 받은 문자열을 순회하면서 index가 q, u, a, c, k 순서대로 들어오게 해서 k까지 얻어지면 cnt하고 다시 순회


def solve(start):
    global cnt
    quack = 'quack'
    j = 0
    first = True

    # q 이니셜을 만나고, 다음 문자열에서 방문하지 않은 index를 start로 하여금 문자열 길이까지 다시 순회한다.
    for i in range(start, len(duck)):
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = True
            # 만약 k까지 찾았으면 cnt하고, j = 0으로 하여금 다시 uack까지 찾게 한다.
            if duck[i] == 'k':
                # first는 quackquack 처럼 연속해서 quack이 나오면 중복을 방지하기 위해서 첫 번째 한번만 나왔을때만 cnt함!
                if first:
                    cnt += 1
                    first = False
                j = 0
                continue
            # k까지 j += 1 해서 찾는다.
            j += 1


if __name__ == "__main__":
    duck = input()
    visited = [False] * len(duck)
    cnt = 0

    # 문자열이 quack 5개로 나누어 떨어져야 제대로 우는 것!
    if len(duck) % 5 != 0:
        print(-1)
        exit()

    # 입력 문자열 만큼 순회하고 첫번째 이니셜인 q이고 visited가 False일때 solve로 i index를 넣는다.
    for i in range(len(duck)):
        if duck[i] == 'q' and not visited[i]:
            solve(i)

    if not all(visited) or cnt == 0:
        print(-1)
    else:
        print(cnt)