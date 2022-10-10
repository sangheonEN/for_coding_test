# 1에서 10000까지의 수 중 8이 들어가는 수 중 8의 갯수의 총 합은?
# 8888 -> 4
# hit: str로 변환해서 count 해보자!

# Method 1
count = 0
for i in range(10001):
    if '8' in str(i):
        count += str(i).count('8')

print(count)

# Method 2
print(str(list(range(1, 10001))).count('8'))


