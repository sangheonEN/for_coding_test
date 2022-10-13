from itertools import permutations
from itertools import combinations
# 중복 허용
from itertools import product
from itertools import combinations_with_replacement
# generator 객체라서 list로 저장해놔야함!


data = ['A', 'B', 'C']

p_result = list(permutations(data, 2))
print(p_result)
p_result.sort(key=lambda x:x[0])
print(p_result)

# list로 변환


c_result = list(combinations(data, 2))
print(c_result)
c_result.sort(key=lambda x:x[0])
print(c_result)

# list로 변환


product_a = list(product(data))
print(product_a)

combinations_with_replacement_b = list(combinations_with_replacement(data, 2))
print(combinations_with_replacement_b)



