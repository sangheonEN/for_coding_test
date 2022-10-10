# N 마리 폰켓몬 중 N/2마리를 가져가도 됨
# 같은 종류의 폰켓몬은 같은 번호 [1, 1, 2, 2] -> 최대 2종류, [3, 3, 3, 3] -> 최대 1종류
# 최대한 다양한 종류의 폰켓몬을 포함하여 N/2마리를 선택
# 1<= len(N) <= 10000 자연수
# 1<= N <= 200000 자연수
# 목적: 선택할 수 있는 폰켄몬 종류 개수의 최댓값을 return

# def solution(nums):
#
#     N = len(nums)
#     arr_1 = len(set(nums))
#
#
#     return arr_1
#
# # set([1, 3, 3, 4]) -> {1, 3, 4} 중복 없는 key를 출력함.
# a = set([8, 8, 8, 8, 4])
#
# print(a)

# # [3, 1, 2, 3] -> 2, [3, 3, 3, 2, 2, 4] -> 3, [3, 3, 3, 2, 2, 2] -> 2
nums = [3, 1, 2, 3]
N = len(nums)
select_num = N / 2
select_arr = list()
count = 0

for i in nums:
    if count != 0:
        if i in select_arr:
            continue

    select_arr.append(i)
    count += 1

final_n = len(select_arr)

print(final_n)
