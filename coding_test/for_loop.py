#%%
# 정수가 주어졌을때, 감소하는 for문 작성
n = 10

for i in range(n, 0, -1):
    print(i-1)

for i in reversed(range(0, 10)):
    print(i)

#%%
# list가 주어졌을때 감소하는 for문 작성
list = [1, 2, 3, 4, 5]

for i in list[::-1]:
    print(i)

#%%
# dict가 주어졌을때 감소하는 for문 작성
dict= {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5
}

print(list(zip(dict.keys(), dict.values())))

"""
Traceback (most recent call last):
    print(list(dict.items))
TypeError: 'list' object is not callable
"""


for key, val in reversed(dict.items()):
    print(key, val)
