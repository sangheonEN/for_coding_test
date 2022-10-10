# N이 1이 될 때까지 두 과정 중 하나를 반복적을 선택하여 수행하려고 한다.
# 단 두번째 연산은 N이 K로 나누어 떨어질 때만 선택
# 1. N에서 1을 뺍니다
# 2. N에서 K로 나눕니다.
# N을 1로 만드는 최소 횟수를 구하라!
# 1 <= N <= 100,000, 2 <= K <= 100,000
import time

N = 100000
K = 789
count = 0
start = time.time()

def first(N):
    return N - 1

def second(N, K):
    return N / K if N % K == 0 else False

while 1:
    if N % K == 0:
        N = N / K
        count += 1
    else:
        N = first(N)
        count += 1

    if N == 1:
        break


end = time.time()
print(count)
print(end-start)