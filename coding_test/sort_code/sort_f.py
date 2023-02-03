#%%
import random

# list 타입 정렬
a = [[random.randint(1, 10), random.randint(1, 10)] for i in range(3)]
print(a)

b = sorted(a, key= lambda x:x[0])
c = sorted(a, key= lambda x:x[1])
print(b)
print(c)

e = [[5, 10], [7, 5], [1, 10]]
f = [[1, 10], [5, 10], [7, 5]]
f2 = [[1, 10], [5, 10], [7, 5]]
g = [[7, 5], [5, 10], [1, 10]]

f = [[1, 10], [5, 10], [7, 5]]
f3 = sorted(f, key=lambda x:(x[1], x[0])) # dim 1 기준으로 솔트하고, dim 0 기준으로 다시 재정렬!
print(f'f3: {f3}')
# f3: [[1, 10], [5, 10], [7, 5]]

f.sort(key = lambda x : x[1])
f2 = sorted(f2, key = lambda x : x[1])
print(f)
print(f2)


#%%
import random

a = [[random.randint(1, 10), random.randint(1, 10)] for i in range(3)]
# dict 타입 정렬
# dict 컴프리핸션 {Key:Value for 요소 in 입력Sequence [if 조건식]}

d = {k : v for k, v in a}
print(d)

d1 = sorted(d.items(), key= lambda x : x[0])
d2 = sorted(d.items(), key= lambda x : x[1])
print(d1)
print(d2)