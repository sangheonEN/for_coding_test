#%%
# list 맨 끝에 원소 추가
a = [1, 2, 3, 4, 5]
a.append(3)
print(a)

a.append(3)



#%%
# list 특정 요소의 index 추출
a = [1, 2, 3, 4, 5, 3]
print(a.index(1))
# list 원소 중 중복되는 index 모두 찾기 -> filter 사용
# filter()는 여러 개의 데이터로 부터 일부의 데이터만 추려낼 때 사용
index_list = list(filter(lambda x: a[x] == 3, range(len(a))))
print(index_list)
#%%
# 문자열 list에서 int로 변경
b = ['1', '2', '3', '4']
#첫번째방법 list컴프리헨션 int("").join(a). "특정문자열".join(리스트)은 특정문자열 기준으로 리스트 원소를 합칠 때 사용함. 합치고 int()씌우고
strtoint_list = [int(("").join(a)) for a in b]
print(strtoint_list)
#두번째방법 map 함수 사용 -> map(함수, iterable변수) iterable변수 하나하나 마다 함수에 입력하여 반환되는 값을 출력함
strtoint_list2 = list(map(int, b))
print(strtoint_list2)

# int list에서 문자열 변경 -> list컴프리헨션 + str()
a = [1, 2, 3, 4, 5]
inttostr_list = [str(c) for c in a]
print(inttostr_list)

#%%
# str split(구분자) -> 구분자 기준으로 str을 나눠서 list의 각 원소로 저장.
str_1 = "1 2 1 3 5 6"
print(str_1)
str_1 = str_1.split(" ")
print(str_1)

#%%
# 문자열을 int 기준으로 정렬하기
a = ["1", "5", "3", "10"]
a.sort(key=lambda x:int(x))
print(a)

#%%
# N차원 list를 1차원 list로 변환하고 정렬하기 sum(iterable변수, 빈리스트[]) [1, 2] + [] = [1, 2]
b = [[[1, 2], [2, 3]], [[4, 5], [1, 1]], [[2, 2],[3, 3]]]
b = sum(b, [])
b = sum(b, [])

import numpy as np

list2 = np.array(b).flatten().tolist()
print(list2)

#%%
# 2차원 list 선언
n = 5
m = 5
d = [[0] * m for _ in range(n)]
print(d)


