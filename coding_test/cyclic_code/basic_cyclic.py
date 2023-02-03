# 기본 순회

s = [1, 3, 4, 6, 8, 14, 18, 27]

# 내가 푼 방법
# 전과 후 수의 차이를 저장
idx = 100

for i in range(len(s) - 1):
    #전
    before = s[i]
    #후
    after = s[i+1]

    if idx > (after - before):
        idx = (after - before)

print(idx)

#%%
# 남이 푼 방법
s = [1, 3, 4, 6, 8, 14, 18, 27]
ss = [3, 4, 6, 8, 14, 18, 27]

set_a = list(zip(s, ss))

set_b = sorted(set_a, key=lambda i: i[1]-i[0])

print(set_b)









