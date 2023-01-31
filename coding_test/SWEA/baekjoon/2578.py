import sys
from collections import OrderedDict

# 줄 띄움 나오면 다음으로 넘어가서 저장
input = sys.stdin.readline

# board = OrderedDict()
board = OrderedDict()
check = [[0] * 5 for i in range(5)]

# board dictionary의 key에는 빙고 숫자. value에는 가로 i, 세로 j index 저장!
for i in range(5):
    bingo = list(map(int, input().split()))
    for j in range(5):
        board[bingo[j]] = (i, j)

cnt = 0

for _ in range(5):
    moderator = list(map(int, input().split()))
    for i in range(5):
        cnt += 1

        # 사회자가 말한 number가 board keys()에 있으면! check에 i, j 인덱스에 1을 넣어서 빙고판 업데이트
        if moderator[i] in board.keys():
            check[board[moderator[i]][0]][board[moderator[i]][1]] = 1

            # bingo cnt
            bingo = 0
            for j in range(5):
                # 가로 축 빙고 count
                if sum(check[j]) == 5:
                    bingo += 1
                # 세로 축 빙고 count
                cnt2 = 0
                for k in range(5):
                    cnt2 += check[k][j]
                    if cnt2 == 5:
                        bingo += 1
            # / 대각선
            cnt3 = 0
            for k in range(5):
                cnt3 += check[k][4-k]
                if cnt3 == 5:
                    bingo += 1
            # \ 대각선
            cnt4 = 0
            for k in range(5):
                cnt4 += check[k][k]
                if cnt4 == 5:
                    bingo += 1
            if bingo >= 3:
                print(cnt)
                sys.exit()
