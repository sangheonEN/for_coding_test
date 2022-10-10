from itertools import permutations
from itertools import combinations
# 순서가 상관있을 경우 permutation
# 예제: 가장 큰 두 자리 수 구하기. 두 수를 선택 하여 가장 큰 두 자리 수를 구하라!
arr = [1, 2, 3, 4]

a = list(permutations(arr, 2))
b = list()
for i in a:
    num = i[0] * 10 + i[1]
    b.append(num)

print(a)
print(max(b))

# 순서가 상관없을 경우 combinations
# 예제: 가장 큰 두 수의 합 구하기

c = list(combinations(arr, 2))
d = list()

for i in c:
    num = i[0] + i[1]
    d.append(num)

print(c)
print(max(d))
