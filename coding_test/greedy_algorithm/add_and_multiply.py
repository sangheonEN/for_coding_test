# x, + 를 이용해서 주어진 수로 만들 수 있는 가장 큰 수를 구하여라!
# 0 ~ 9 사이의 str 문자열로 수가 주어짐
# 가장 큰 수는 20억 이하 정수
# 1 <= S의 길이 <= 20

s = "02984"
result = int(s[0])

for i in s:
    i=int(i)
    
    if i == 0 or i == 1:
        result += i
    else:
        result *= i

print(result)

