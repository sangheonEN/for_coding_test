# 소수는 for 문으로 탐색했을때 자기 자신으로 나누었을때 나머지가 0이 안될때만 가능!
from itertools import permutations
from itertools import combinations


# 주어진 수 하나씩 문자열 list만들기
# 순열 list 만들기
# 소수 판별하기

def solution(numbers):
    numbers_list = list()

    for num in numbers:
        numbers_list.append(num)

    permu_list = list()

    for i in range(1, len(numbers_list) + 1):
        permu_list += list(permutations(numbers_list, i))

    # b = [''.join(p) for p in permu_list]
    # print(b)

    new_int_list = [int(("").join(p)) for p in permu_list]

    new_int_set = set(new_int_list)
    new_int_list = list(new_int_set)
    print(new_int_list)

    decimal_count = 0
    for i in new_int_list:
        if i < 2:
            continue
        # 내가 실수한 부분 int(i ** 0.5) + 1 까지 순회해야되는데 max(new_int_list)로 해버림.
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                decimal_count -= 1
                break

        # break 뒤에도 연산이 넘어가서 +=1 되버림 그래서 소수가 아닌 경우 -1을 해주어야함.
        decimal_count += 1

    return decimal_count


a = solution("011")

print(a)

