
# map 크기 M, 치킨집 최대 선택가능 개수 N
N, M = map(int, input().split())

# map 2d input data load!!
map_2d = [list(map(int, input().split())) for _ in range(N)]
print(map_2d)

# N은 행, M은 열
map_1d = [[False]*M for _ in range(N)]
print(map_1d)