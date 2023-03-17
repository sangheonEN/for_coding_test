"""

# 시작지점-술래:중앙, 도망자: 지정 (중앙 x)
# m명 도망자 이동방향: 유형1 상하(항상 아래쪽 보고 시작), 유형2 좌우(항상 오른쪽 보고 시작)
# h개의 나무 존재. 나무는 술래 및 도망자 위치와 겹칠 수 있음.

# 게임 순서
k번 만큼 1. 2. 반복

1. m명의 도망자 먼저 이동
   - 도망자 이동 조건: 현재 술래와의 거리가 3이하인 도망자. 도망자 위치(x1, y1)이고 술래 위치(x2, y2)라면, 둘 사이 거리 = |x1- x2| + |y1 - y2|
   - 이동 방법
     1) 격자 벗어나지 않는 경우
        * 움직이려는 칸에 술래 있으면 이동 X
        * 없다면, 이동. (나무와는 무관)
     2) 격자 벗어나는 경우
        * 반대 방향으로 틀고 술래가 있다면 이동 X -> 일단 방향은 무조건 변경.
        * 없다면, 이동. (나무와는 무관)

2. 술래 이동
   - 윗방향으로 시작해서 시계 방향으로 달팽이 모양으로 한칸 이동
   - 끝까지 이동 시 반 시계 방향으로 달팽이 모양으로 한칸 이동
   - 이동 후의 위치가 방향을 트는 지점이면 바로 방향을 변경

2-1. 도망자 잡기
   - 이동 직후 시야내에 있는 도망자 잡기. 시야는 현재 칸을 포함해서 항상 3칸, 나무랑 같은 격자에 있는 도망자 빼고 다 잡음
   - 술래는 현재 턴을 t번째 턴이라고 했을때 (t x 잡힌 도망자의 수) 만큼 점수를 획득.
   - 잡힌 도망자는 격자에서 사라짐

"""

def is_grid(x, y):

    return 0 <= x and x < n and 0 <= y and y < n


def hider_move():

    for i in range(m):
        x, y, d = hider[i]

        if (abs(seeker_position[0] - x) + abs(seeker_position[1] - y)) <= 3:
            #move
            nx = x + dx[d]
            ny = y + dy[d]
            if is_grid(nx, ny):
                # 방향 전환 x, 움직이려는 칸에 술래 있으면 이동 x
                if nx == seeker_position[0] and ny == seeker_position[1]:
                    pass
                else:
                    # 도망자 이동
                    hider[i] = nx, ny, d
            else:
                # 방향 전환 o, 움직이려는 칸에 술래 있으면 이동 x
                d = (d + 2) % 4

                if nx == seeker_position[0] and ny == seeker_position[1]:
                    pass
                else:
                    # 도망자 이동
                    hider[i] = nx, ny, d
        else:
            pass


def seeker_move():
    

    pass


def hider_grap(t):


    pass


def simulation(t):

    # 도망자 이동
    hider_move()

    # 술래 이동
    seeker_move()

    # 술래가 도망자 잡기
    hider_grap(t)

    pass



if __name__ == "__main__":

    # n:격자 크기, m: 도망자수, h: 나무 수, k: 턴 수 입력
    n, m, h, k = map(int, input().split())

    # m개의 줄에 거쳐 도망자 위치 x, y 및 이동 방법 d 입력 ex) 0번째 runner 위치 및 이동 방향 -> runner[0] = x, y, d
    hider = [[] for _ in range(m)]
    for i in range(m):
        hider[i] = list(map(int, input().split()))

    # h개의 줄에 거쳐 나무 위치 입력 ex) 0번째 tree 위치 -> tree[0] = x, y
    tree = [[] for _ in range(h)]
    for j in range(h):
        tree[j] = list(map(int, input().split()))

    # print(n, m, h, k)
    # print(runner)
    # print(tree)

    # 상, 우, 하, 좌.
    # 이렇게 설정하는 이유. 도망자 이동 방향: 1은 우, 2는 하로 설정
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 술래 위치 및 이동 방향
    seeker_position = (n // 2, n // 2)
    seeker_direction = True # True: 시계방향, False: 반시계방향

    # score
    score = 0

    # 총 k턴 만큼 시뮬레이션 시작
    for t in range(k):
        simulation(t+1)
