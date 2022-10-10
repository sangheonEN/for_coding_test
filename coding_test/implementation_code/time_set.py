# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각
# 0 <= N <= 23

#%%
print(True if '3' in str(53) else False)

#%%
N = 5
count = 0

for hour in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(s)+str(m)+str(hour):
                count+=1

print(count)