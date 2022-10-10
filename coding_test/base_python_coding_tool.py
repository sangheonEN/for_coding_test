# hash는 dict로!!

def solution(phone_book):

    answer = phone_book

    return answer

import time
start = time.process_time()

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])

end = time.process_time()
print(f"time: {end-start}")

print(1e9)


a = [file for file in range(0, 11) if file%2 == 1]
print(a)

#2차원 list 만들기
m = 5
n = 5

arr = [[0]*m for _ in range(n)]

print(arr)

arr[1][1] = 5
print(arr)

arr[1].remove(5)
print(len(arr[1]))

arr.sort()
print(arr)

# 집합 자료형
arr2 = [i for i in range(11)]
remove_set = {3, 6}
print(arr2)
arr3 = [i for i in arr2 if i not in remove_set]
print(arr3)

print("zz"*5)

# 튜블 자료형
# 해싱의 키값, 서로 다른 성질의 데이터, 메모리 효율적

tu1 = (1, 2, 3, 4, 5, 6)

print(tu1)


# dict

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

data5 = dict()
data5[1] = "apple"
data5[2] = "bb"
data5[3] = 5



for i in range(10):

    data5[i] = "bb"

print(data5)
print(data)

if '사과' in data:
    print("True")
else:
    print(False)

print(data.keys())
print(data.values())

for key in data.keys():
    print(type(data[key]))

# set 중복 허용 x, 순서 없음 -> 데이터가 존재하는지 존재하지 않는지 체크할 때 사용
data2 = set([1,2,3,4,5,6])
data3 = set([1, 1, 2, 3, 4, 5])
print(data2)

# 합집합, 교집합, 차집합
print(data2 | data3)
print(data2 & data3)
print(data2 - data3)

# lambda 표현식
# (lambda 입력변수: 출력변수)(입력 매개 변수)
# (lambda a, b: a+b)(3, 5)
print((lambda a, b: a+b)(3, 5))

#%%
# {행, 열} 2차원 map 만들기
for i in range(5):
    for j in range(5):
        print('(',i, ',', j,')', end=' ')
    print()

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# now position
x, y = 2, 2

for i in range(4):
    # next position

    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)
