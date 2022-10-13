# 2차원 정방행렬에 대한 값을 회전해보자!

def rotated(a):
    # 새로운 result 0의 원소를 가진 2차원 빈리스트 생성
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    # n, m 만큼 반복하면서 result update
    # 세로로 수행
    # result[j]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


if __name__ == "__main__":

    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    b90 = rotated(arr)
    c180 = rotated(b90)
    d270 = rotated(c180)
    print(arr)
    print(b90)
    print(c180)
    print(d270)


