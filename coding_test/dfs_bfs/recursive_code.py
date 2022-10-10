
def recursive_f(count):
    print("재귀함수!!")
    if count == 10:
        return

    recursive_f(count+1)

recursive_f(1)


def factorial_f(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

print(factorial_f(5))

def factorial_recursive_f(n):

    if n <= 1:
        return 1

    return n * factorial_f(n-1)

print(factorial_recursive_f(5))

# 유클리드 호제법 최대 공약수 구할때 사용
# 두 자연수 A, B에서 (A>B) A를 B로 나눈 나머지를 R이라 하고 이때 A와 B의 최대 공약수와 B와 R의 최대공약수는 같다
# 재귀함수로 구현가능

def gcd(a, b):
    print(a, b)

    if a % b == 0:
        return b

    else:
        return gcd(b, a % b)

print(gcd(192, 162))



