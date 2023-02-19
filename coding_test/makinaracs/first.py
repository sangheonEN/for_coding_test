# n개의 옷을 배송
# 옷 3개, 5개를 담을 수 있는 상자 있음
# 상자 크기 상관 없이, 상자의 개수로 배송비 청구, 상자의 개수를 최소한으로 줄이려고함!
# 옷을 꽉 채워서 상자를 만들어야 배송 가능
"""
입력
n: 옷의 개수

return: 배송비를 최소화할 수 있는 상자 개수

어떠한 방법으로도 보낼 수 없으면 -1 return

"""
n = 24
print(n // 5)
print(n % 5)

n = 15
answer = 0

def minimize_shipping_boxes(n):
    # 초기값으로 모든 dp 값을 -1로 설정
    dp = [-1] * (n+1)

    # 0개의 옷을 보내는 경우, 상자가 필요하지 않으므로 dp[0] = 0으로 설정
    dp[0] = 1

    for i in range(1, n+1):
        if i >= 3 and dp[i-3] != -1:
            dp[i] = dp[i-3] + 1
        if i >= 5 and dp[i-5] != -1:
            dp[i] = dp[i-5] + 1
        else:
            dp[i] = min(dp[i], dp[i-5] + 1)

        print(dp)

    return dp[n]

print(minimize_shipping_boxes(1029))