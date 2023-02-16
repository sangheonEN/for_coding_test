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


# Player p의 정보를 갱신해줍니다.
def update(cur_player_num, nx, ny, nd, s, better_gun_damage):
    p = cur_player_num, nx, ny, nd, s, better_gun_damage

    # Player의 위치를 찾아
    # 값을 갱신해줍니다.
    for i in range(m):
        num_i, _, _, _, _, _ = player_arr[i]

        if num_i == cur_player_num:
            player_arr[i] = p
            break


def loser_move(lose_player):
    num, x, y, d, s, gun_damage = lose_player
    # 총 내려놓기
    try:
        board[x][y] = gun_damage

    except Exception as e:
        if e == 'IndexError: list assignment index out of range':
            pass

    # 빈 공간을 찾아 이동
    # 기존 방향으로 이동해보고, 격자 바깥으로 가거나 이동했을때 사람이 있을 경우, 90도 회전해서 이동.
    for i in range(len(dx)):
        nx = x + dx[d]
        ny = y + dy[d]
        if is_range(nx, ny):
            for j in range(m):
                if nx == player_arr[j][1] and ny == player_arr[j][2]:  # player가 있는 경우
                    # 90도 회전 어차피 dx, dy는 순서대로 90도로 회전한다. 그런데, 4로 왔을때 0으로 변환하기 위해 % 사용
                    nd = (d + i) % 4
                    nx = nx + dx[nd]
                    ny = ny + dy[nd]
                    loser_move([num, nx, ny, nd, s, 0])

                else: # player가 없는 경우
                    # move
                    nx, ny, nd = move_player(nx, ny, d)
                    better_gun_damage = gun_grap(nx, ny, 0)
                    update(num, nx, ny, nd, s, better_gun_damage)
                    return

        else: # 격자 바깥으로 나갈 경우
            # 90도 회전 어차피 dx, dy는 순서대로 90도로 회전한다. 그런데, 4로 왔을때 0으로 변환하기 위해 % 사용
            nd = (d + i) % 4
            nx = nx + dx[nd]
            ny = ny + dy[nd]
            loser_move([num, nx, ny, nd, s, 0])


def fight(player1, player2, nx, ny):
    pn1, _, _, pd1, ps1, p1_gun_damage = player1
    pn2, _, _, pd2, ps2, p2_gun_damage = player2

    # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
    # 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
    # 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득

    if ps1+p1_gun_damage > ps2 + p2_gun_damage: # p1 승
        pp[pn1] += (ps1+p1_gun_damage) - (ps2 + p2_gun_damage)
        loser_move(player2)
        # winner gun_grap
        better_gun_damage = gun_grap(nx, ny, p1_gun_damage)
        update(pn1, nx, nx, pd1, ps1, better_gun_damage)
    elif ps1+p1_gun_damage < ps2 + p2_gun_damage: # p2 승
        pp[pn2] += (ps2+p2_gun_damage) - (ps1 + p1_gun_damage)
        loser_move(player1)
        # winner gun_grap
        better_gun_damage = gun_grap(nx, ny, p2_gun_damage)
        update(pn2, nx, nx, pd2, ps2, better_gun_damage)
    else: # 동률일 경우
        if ps1 > ps2: # p1 승
            pp[pn1] += (ps1 + p1_gun_damage) - (ps2 + p2_gun_damage)
            loser_move(player2)
            # winner gun_grap
            better_gun_damage = gun_grap(nx, ny, p1_gun_damage)
            update(pn1, nx, nx, pd1, ps1, better_gun_damage)

        else: # p2 승
            pp[pn2] += (ps2 + p2_gun_damage) - (ps1 + p1_gun_damage)
            loser_move(player1)
            # winner gun_grap
            better_gun_damage = gun_grap(nx, ny, p2_gun_damage)
            update(pn2, nx, nx, pd2, ps2, better_gun_damage)


def gun_grap(nx, ny, gun_damage):
    # 이동할 위치에 gun이 있으면, 총 줍기. 만약 내가 총 가지고 있으면, 데미지 비교해서 교체하기.
    if board[nx][ny] and gun_damage: # 이동 위치에 gun이 있는데, 내가 총을 가지고 있는 경우
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
        d = (d + 2) if d < 2 else (d - 2)
        nx = -nx
        ny = -ny

    return nx, ny, d


def simulate():

    for i in range(m):
        cur_player_num, x, y, d, s, gun_damage = player_arr[i]

        # step 1: 현재 플레이어의 다음 위치로 이동. 격자 벗어나면 반대 방향으로 이동.
        nx, ny, nd = move_player(x, y, d)

        # 이동한 방향에 플레이어가 없는 경우, 총 줍기 수행. 있는 경우 결투.
        for j in range(m):
            if nx == player_arr[j][1] and ny == player_arr[j][2]: # 이동 방향에 플레이어 존재. 결투 시작
                # 현재 플레이어 update 해주고 싸워야함.
                better_gun_damage = gun_grap(nx, ny, gun_damage)
                update(cur_player_num, nx, ny, nd, s, better_gun_damage)
                # 현재 player 업데이트하고 나서 결투 진행
                fight(player_arr[i], player_arr[j], nx, ny)
            else: # 이동 방향에 플레이어 존재하지 않음. 총 줍기
                # step 2: 이동 위치에 총 있는지 확인. 있으면, 총 줍기, 없으면 pass. 근데, 내가 총을 가지고 있는데 이동 위치에 총이 있으면, 그 총의 데미지와 내 총의 데미지를 비교하여 큰 값으로 갱신하고 나머지는 해당 위치에 둔다.
                better_gun_damage = gun_grap(nx, ny, gun_damage)
                update(cur_player_num, nx, ny, nd, s, better_gun_damage)

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


    # k번에 걸쳐 시뮬레이션을 진행합니다.
    for _ in range(k):
        simulate()

    # 각 플레이어가 획득한 포인트를 출력합니다.
    for point in pp:
        print(point, end=" ")




