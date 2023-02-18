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

    # Player의 정보를 갱신
    for i in range(m):
        player_num, x, y, _, _, _ = player_arr[i]

        if player_num == cur_player_num:
            #player_arr에 저장된 player 고유 정보 갱신
            player_arr[i] = p
            break




def loser_move(num, x, y, d, s, gun_damage):

    # 총 가지고 있을때만, 총 내려놓기
    if gun_damage != 0:
        gun_board[x][y].append(gun_damage)
        gun_damage = 0
    else:
        pass

    # 빈 공간을 찾아 이동
    # 기존 방향으로 이동해보고, 격자 바깥으로 가거나 이동했을때 사람이 있을 경우, 90도 회전해서 이동.
    nx = x + dx[d]
    ny = y + dy[d]
    if is_range(nx, ny) or find_player(nx, ny): # 격자 바깥으로 나갈 경우 or player가 있을 경우 회전.
        # 90도 회전 어차피 dx, dy는 순서대로 90도로 회전한다. 그런데, 4로 왔을때 0으로 변환하기 위해 % 사용
        loser_move(num, x, y, (d + 1) % 4, s, gun_damage)

    else: # player가 없거나, 격자 바깥으로 나가지 않을때!
        # move
        better_gun_damage = gun_grap(nx, ny, gun_damage)
        # player_position의 위치 정보를 갱신 -> 이전 좌표가 필요해서 먼저 갱신
        player_position_update(num, nx, ny)
        update(num, nx, ny, d, s, better_gun_damage)
        return



def fight(player1, player2, nx, ny):
    pn1, px1, py1, pd1, ps1, p1_gun_damage = player1 # 이동할 놈
    pn2, px2, py2, pd2, ps2, p2_gun_damage = player2 # 이동할 격자에 이미 존재하는 놈

    # 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합을 비교하여 더 큰 플레이어가 이기게 됩니다.
    # 만일 이 수치가 같은 경우에는 플레이어의 초기 능력치가 높은 플레이어가 승리하게 됩니다.
    # 이긴 플레이어는 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이만큼을 포인트로 획득

    if ps1 + p1_gun_damage > ps2 + p2_gun_damage: # p1 승
        pp[pn1] += (ps1 + p1_gun_damage) - (ps2 + p2_gun_damage)
        player_position[px1][py1] = 0
        loser_move(pn2, px2, py2, pd2, ps2, p2_gun_damage)
        # winner update: 총 교체
        player_position_update(pn1, nx, ny)
        better_gun_damage = gun_grap(nx, ny, p1_gun_damage)
        update(pn1, nx, ny, pd1, ps1, better_gun_damage)
    elif ps1 + p1_gun_damage < ps2 + p2_gun_damage: # p2 승
        pp[pn2] += (ps2+p2_gun_damage) - (ps1 + p1_gun_damage)
        player_position[px1][py1] = 0
        loser_move(pn1, nx, ny, pd1, ps1, p1_gun_damage)
        # winner gun_grap
        better_gun_damage = gun_grap(nx, ny, p2_gun_damage)
        update(pn2, nx, ny, pd2, ps2, better_gun_damage)
    else: # 동률일 경우
        if ps1 > ps2: # p1 승
            pp[pn1] += (ps1 + p1_gun_damage) - (ps2 + p2_gun_damage)
            player_position[px1][py1] = 0
            loser_move(pn2, px2, py2, pd2, ps2, p2_gun_damage)
            # winner update: 총 교체
            player_position_update(pn1, nx, ny)
            better_gun_damage = gun_grap(nx, ny, p1_gun_damage)
            update(pn1, nx, ny, pd1, ps1, better_gun_damage)
        else: # p2 승
            pp[pn2] += (ps2 + p2_gun_damage) - (ps1 + p1_gun_damage)
            player_position[px1][py1] = 0
            loser_move(pn1, nx, ny, pd1, ps1, p1_gun_damage)
            # winner gun_grap
            better_gun_damage = gun_grap(nx, ny, p2_gun_damage)
            update(pn2, nx, ny, pd2, ps2, better_gun_damage)


def gun_grap(nx, ny, gun_damage):
    """

    :param nx: 이동할 x 좌표
    :param ny: 이동할 y 좌표
    :param gun_damage: 내가 지금 가지고 있는 gun damage. 0이면 가지고 있지 않음.
    :return: 교체할 gun damage
    """

    # 이동할 위치에 gun이 있으면, 총 줍기. 만약 내가 총 가지고 있으면, 데미지 비교해서 교체하기.
    if gun_board[nx][ny] and gun_damage: # 이동 위치에 gun이 있는데, 내가 총을 가지고 있는 경우
        # 가지고 있는 총과 놓여 있는 총들 중에 제일 데미지가 큰 총과 비교해서, 놓여 있는 총과 내 총을 비교해서 교체한다.
        if max(gun_board[nx][ny]) > gun_damage:
            gun_board[nx][ny].append(gun_damage)
            gun_board[nx][ny].sort(reverse=True)
            better_gun_damage = gun_board[nx][ny][0]
            gun_board[nx][ny].pop(0)
        else:
            better_gun_damage = gun_damage

    # 총을 안가지고 있으면 놔둘 총이 없으니 append 구문을 배제해야함.
    elif gun_board[nx][ny] and gun_damage == 0: # 이동 위치에 gun이 있는데, 내가 총을 안가지고 있을 경우
        gun_board[nx][ny].sort(reverse=True) # board에 남아 있는 총을 오름차순으로 정렬해서
        better_gun_damage = gun_board[nx][ny][0] # 해당 보드의 가장 높은 데미지 총을 가짐
        gun_board[nx][ny].pop(0) # 가장 큰 총 뺀다.

    else: # 이동 위치에 총이 없는 경우, 가지고 있는 총을 그냥 가짐.
        better_gun_damage = gun_damage

    return better_gun_damage


def is_range(nx, ny):

    return nx < 0 or ny < 0 or nx >= n or ny >= n

def move_player_position(x, y, d):

    nx = x + dx[d]
    ny = y + dy[d]

    # 격자 넘어가면 반대 방향으로 이동
    if is_range(nx, ny): # False이면, 격자 안에 있는거! True이면, 격자 바깥으로 벗어남.
        # d = 0 위쪽 2 아래
        d = (d + 2) if d < 2 else (d - 2)
        ### 격자 반대 방향으로 이동한 좌표 찾기
        nx = x + dx[d]
        ny = y + dy[d]

    return nx, ny, d


def player_position_update(player_num, nx, ny):
    """
    :param player_num: player 번호
    :param x: 움직이기 전 x좌표
    :param y: 움직이기 전 y좌표
    :param nx: 움직인 후 x좌표
    :param ny: 움직인 후 y좌표
    """
    # 원래 있던 위치 0으로 초기화, 이동 위치 player number로 갱신
    player_position[nx][ny] = player_num + 1 # + 1은 player_position의 플레이어 번호는 1부터 시작하기 때문에.


def find_player(nx, ny):
    """

    :param x: 플레이어가 이동할 x 좌표
    :param y: 플레이어가 이동할 y 좌표
    :return: 이동할 좌표에 플레이어가 존재하면 True, 존재하지않으면, False
    """
    if not player_position[nx][ny]:
        return 0
    else:
        player_num = player_position[nx][ny]
        return player_num


def simulate():

    for i in range(m):
        cur_player_num, x, y, d, s, gun_damage = player_arr[i]

        # step 1: 현재 플레이어의 다음 위치로 이동. 격자 벗어나면 반대 방향으로 이동.
        nx, ny, nd = move_player_position(x, y, d)
        # 방향만 업데이트
        update(cur_player_num, x, y, nd, s, gun_damage)

        # 이동 방향에 플레이어 존재 여부 확인. 존재하면 True, 존재하지 않으면 False
        find_flag = find_player(nx, ny) # find_flag는 0 또는 player의 number
        if find_flag:
            # 존재하면, 싸움시작. 싸움하고, 이기고, 진 player마다 업데이트까지 수행!
            # find_flag - 1 이유는 find_flag에서 플레이어가 있을때, 1~m+1사이의 값을 return 하기 때문에, player_arr의 0~m 인덱스를 맞추기 위해.
            fight(player_arr[i], player_arr[find_flag - 1], nx, ny)
        else: # 존재하지 않으면, 이동하고 총 줍기.
            # 총 줍기
            better_gun_damage = gun_grap(nx, ny, gun_damage)
            # player 정보 업데이트
            update(cur_player_num, nx, ny, nd, s, better_gun_damage)
            # player_position의 위치 정보를 갱신 -> 이전 좌표가 필요해서 먼저 갱신
            player_position[x][y] = 0
            player_position_update(cur_player_num, nx, ny)


if __name__ == "__main__":

    # n: 격자 크기, m 플레이어 수, k 라운드 수
    n, m, k = map(int, input().split())
    # print(n, m, k)


    # map load board 원소 값은 놓여 있는 총의 데미지이고, 총이 쌓인다.
    # gun 정보 arr 저장 총을 쌓기 위해서 Dim 3차원 배열로 선언.
    gun_board = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        board = list(map(int, input().split()))
        for j in range(n):
            if board[j] != 0:
                gun_board[i][j].append(board[j])


    # player data [player_num, x, y, d, s, gun_damage]
    player_arr = []
    for player_num in range(m):
        x, y, d, s = tuple(map(int, input().split()))
        player_arr.append((player_num, x-1, y-1, d, s, 0))


    # 플레이어의 최신 위치 정보를 저장해놓음. visited arr에 플레이어 번호를 x, y 좌표에 저장.
    player_position = [[0]*n for i in range(n)]
    # 초기 position 저장
    for _ in range(m):
        player_position[player_arr[_][1]][player_arr[_][2]] = player_arr[_][0]+1


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





"""
def gun_grap()에서 하드코딩한걸 변경함.
        # 하드코딩
        # if max(gun_board[nx][ny]) < gun_damage: # 격자에 놓인 총들보다 내 총 데미지가 더 큼 pass
        #     better_gun_damage = gun_damage
        # elif max(gun_board[nx][ny]) > gun_damage:
        #     board[nx][ny].append(gun_damage)
        #     board[nx][ny].sort(reverse=True)
        #     better_gun_damage = board[nx][ny][0]
        #     board[nx][ny].pop(0)
        # else: # 격자에 놓인 총들 중 가장 큰 데미지를 가진 총과 내 총 데미지를 비교해도 같아서 pass
        #     better_gun_damage = gun_damage
        
        # 변경
        if max(gun_board[nx][ny]) > gun_damage:
            board[nx][ny].append(gun_damage)
            board[nx][ny].sort(reverse=True)
            better_gun_damage = board[nx][ny][0]
            board[nx][ny].pop(0)
        else:
            better_gun_damage = gun_damage
        
        
"""
