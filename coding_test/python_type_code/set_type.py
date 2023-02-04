#%%
# 중복 제거되고 순서를 무시한 채 랜덤으로 출력됨. 그래서 중복 제거 필터로 사용함.
a = set([2, 1, 1, 1, 11, 2, 3, 4, 4, 4, 4, 4])

a1 = list(a)
a1.sort()
print(a1)

print(a)

b = set(["a", "a", "b", "c", "a", "b"])
print(b)

b1 = list(b)

b1.sort()

print(b1)