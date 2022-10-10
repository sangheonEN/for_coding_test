# 거스름 돈 수 count

# 500, 100, 50, 10원 짜리 동전으로 거스르는데 큰 단위부터 작은 단위로

fee = 1260
count = []

arr = [500, 100, 50, 10]

for coin in arr:
    count += fee // coin
    fee %= coin
    print(f"coin : {coin}, count: {count}")

print(f"total count: {count}")

# 시간 복잡도는 동전의 총 종류로 결정됨! O(N)