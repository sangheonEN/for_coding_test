# 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여!
# N명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날 수 있는 그룹 수의 최댓값은?
# 모든 모험가를 특정한 그룹에 넣을 필요 없다.
import time

start = time.time()

scare_arr = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
scare_arr.sort()
count = 0
group_num = 0

for i in scare_arr:
    count += 1
    if count >= i:
        group_num += 1
        count = 0

end = time.time()

print(group_num)
print(end - start)
