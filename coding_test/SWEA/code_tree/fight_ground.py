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

def simulate():

    for i in range(m):
        player_num, x, y, d, s, gun_damage = player_arr[i]

        # step 1: 현재 플레이어의 다음 위치와 방향을 갱신.


        # step 2: 해당 위치에 있는 전체 플레이어의 정보를 얻어옴.

        # step 3: 현재 플레이어의 위치와 방향을 보정.

        # step 4: 플레이어 위치 이동, 이동한 위치에 플레이어가 없다면, 이동하고 있다면, 결투 진행

if __name__ == "__main__":

    # n: 격자 크기, m 플레이어 수, k 라운드 수
    n, m, k = map(int, input().split())
    print(n, m, k)

    # map load
    board = [list(map(int, input().split())) for i in range(n)]
    print(board)

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




