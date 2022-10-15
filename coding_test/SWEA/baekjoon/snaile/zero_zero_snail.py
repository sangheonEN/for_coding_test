def snail(n, m):
    arr = [[0]*m for _ in range(n)]
    row = 0
    col = -1
    cnt = 1
    trans = 1
    # n이 0보다 작아지면 도달
    while n > 0 and m > 0:
        # n 열만큼 가로로 cnt를 넣으면서 이동 하나씩 이동할때마다 cnt+=1
        for i in range(m):
            col += trans
            arr[row][col] = cnt
            cnt += 1

        # n열만큼 이동후 n-1행만큼 세로로 cnt를 넣으면서 이동
        n -= 1
        for j in range(n):
            row += trans
            arr[row][col] = cnt
            cnt += 1
        m -= 1
        # 반대 방향으로 index 줄이면서 이동!
        trans *= -1

    return arr

n = 5
m = 4
arr = snail(n, m)
print(" ".join(map(str, arr)))
