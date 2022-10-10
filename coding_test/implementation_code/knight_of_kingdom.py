# 1~8, a~h map
# a->가로니까 y값으로 변경, 1->세로니까 x값으로 변경
x = input()

n = x[0]
m = x[1]

str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(0, 8):
    if str_list[i] == n:
        n = i+1

dx = [-1, -1, 1, 1, -2, 2, -2, 2]
dy = [2, -2, -2, 2, -1, -1, 1, 1]

# 2차원 벡터로도 사용가능!
move_steps = [[-1, 2], [-1, -2], [1, -2], [1, 2], [-2, -1], [2, -1], [-2, 1], [2, 1]]

x = int(m)
y = int(n)

count = 0

for i in range(0, len(str_list)):

    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    count += 1


print(count)



