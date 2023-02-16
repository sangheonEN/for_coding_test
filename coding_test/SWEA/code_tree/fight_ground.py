"""


입력
1. n은 격자의 크기, m은 플레이어의 수, k는 라운드의 수
2. n개의 줄에 걸쳐 격자에 있는 총의 정보
3. m개의 줄에 걸쳐 플레이어들의 정보 x, y, d, s -> x, y는 플레이어 위치, d는 방향, s는 플레이어 초기 능력치
   * 방향 d는 0부터 3까지 순서대로 0:↑, 1:→, 2:↓, 3:← 의미
   * 각 플레이어의 초기 능력치는 모두 다릅니다.
   * 각 플레이어의 위치는 겹쳐져 주어지지 않으며, 플레이어의 초기 위치에는 총이 존재하지 않습니다.

예시
5 4 1
1 2 0 1 2
1 0 3 3 1
1 3 0 2 3
2 1 2 4 5
0 1 3 2 0
1 3 2 3
2 2 1 5
3 3 2 2
5 1 3 4

출력
k 라운드 동안 게임을 진행하면서 각 플레이어들이 획득한 포인트를 공백을 사이에 두고 출력

해야할 일
1.
2.
3.

"""

def fight():
    pass

def gun_grap(nx, ny, gun_damage):
    # 이동할 위치에 gun이 있으면, 총 줍기. 만약 내가 총 가지고 있으면, 데미지 비교해서 교체하기.
    if board[nx][ny] and gun_damage: # 이동 위치에 gun이 있는데, 내가 총을 가질 경우
        better_gun_damage = max(board[nx][ny], gun_damage) # 데미지가 더 큰 총을 가짐
        board[nx][ny] = min(board[nx][ny], gun_damage) # board에 총을 놔둠

    elif board[nx][ny]: # 이동 위치에 gun이 있는데, 내가 총을 안가지고 있을 경우
        better_gun_damage = board[nx][ny] # 해당 보드의 총을 가짐
        board[nx][ny] = 0 # 해당 board에 총이 없어짐

    else: # 이동 위치에 총이 없는 경우.
        better_gun_damage = gun_damage

    return better_gun_damage


def is_range(nx, ny):

    return 0 <= nx and nx < n and 0 <= ny and ny < n

def move_player(x, y, d):

    nx = x + dx[d]
    ny = y + dy[d]

    # 격자 넘어가면 반대 방향으로 이동
    if not is_range(nx, ny):
        nx = -nx
        ny = -ny

    return nx, ny


def simulate():

    for i in range(m):
        player_num, x, y, d, s, gun_damage = player_arr[i]

        # step 1: 현재 플레이어의 다음 위치로 이동. 격자 벗어나면 반대 방향으로 이동.
        nx, ny = move_player(x, y, d)

        # 이동한 방향에 플레이어가 없는 경우, 총 줍기 수행. 있는 경우 결투.
        for _, px, py, _, _, _ in player_arr:
            if nx == px and ny == py: # 이동 방향에 플레이어 존재. 결투 시작
                fight()
            else: # 이동 방향에 플레이어 존재하지 않음. 총 줍기
                # step 2: 이동 위치에 총 있는지 확인. 있으면, 총 줍기, 없으면 pass. 근데, 내가 총을 가지고 있는데 이동 위치에 총이 있으면, 그 총의 데미지와 내 총의 데미지를 비교하여 큰 값으로 갱신하고 나머지는 해당 위치에 둔다.
                better_gun_damage = gun_grap(nx, ny, gun_damage)




        # step 3: 해당 위치에 있는 전체 플레이어의 정보를 얻어옴. 이동한 위치에 플레이어가 격돌하는지 보기 위해



        # step 3: 현재 플레이어의 위치와 방향을 보정.

        # step 4: 플레이어 위치 이동, 이동한 위치에 플레이어가 없다면, 이동하고 있다면, 결투 진행

        pass

if __name__ == "__main__":

    # n: 격자 크기, m 플레이어 수, k 라운드 수
    n, m, k = map(int, input().split())
    # print(n, m, k)

    # map load
    board = [list(map(int, input().split())) for i in range(n)]
    # print(board)

    # player data [player_num, x, y, d, s, gun_damage]
    player_arr = []
    for player_num in range(m):
        x, y, d, s = tuple(map(int, input().split()))
        player_arr.append((player_num, x-1, y-1, d, s, 0))

    # 방향 d -> 0:↑, 1:→, 2:↓, 3:←
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # player의 포인트 정보 저장
    pp = [0] * m

    # 선언 이유 찾기 아직 모르겠음.
    EMPTY = (-1, -1, -1, -1, -1, -1)

    # k라운드 만큼 시뮬레이션 수행
    for _ in range(k):
        simulate()

    #




