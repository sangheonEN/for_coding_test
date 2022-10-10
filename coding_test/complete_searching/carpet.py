

# 처음에 문제를 잘못보고 노란색 격자의 위치는 상관 없는 줄 알았다.
# 하지만, 갈색 격자가 노란색 격자를 둘러 싸는 형태의 직사각형 형태의 카팻으로 확인해서 재풀이함. -> 문제를 정확히 파악하고 코딩하자!

def solution(brown, yellow):

    total = brown + yellow

    for b in range(1, total+1):

        if total % b == 0:
            a = int(total / b)
            if (2 * a) + (2 * b) - 4 == brown:
                break
        else:
            continue

    if a < b:
        temp = a
        a = b
        b = temp

    return [a, b]


list_2 = solution(10, 2)
print(list_2)


# 약수로 접근했다가 다시 방정식으로 제약조건을 걸어서 break 구문을 형성하여 완전탐색에서 알맞는 중단 기준을 설정함.
def solution(brown, yellow):
    answer = []

    z = brown + yellow

    yacsu = []

    for i in range(1, z + 1):
        if z % i == 0:
            a = int(z / i)
            if (2 * a) + (2 * i) - 4 == brown:
                yacsu.append(a)
                yacsu.append(i)
                break

    return [yacsu[0], yacsu[1]]


# def solution(brown, yellow):
#     answer = []
#
#     z = brown + yellow
#
#     yacsu = []
#
#     for i in range(1, z + 1):
#         if z % i == 0:
#             a = int(z / i)
#             if (2 * a) + (2 * i) - 4 == brown:
#                 yacsu.append(i)
#                 break
#
#     # len이 짝수일때는 중간 두 값의 크기
#     # len이 홀수일때는 중간값 * 중간값이 크기
#
#     if len(yacsu) % 2 == 0:
#         mid2 = len(yacsu) // 2
#         mid1 = mid2 - 1
#         x = yacsu[mid2]
#         y = yacsu[mid1]
#
#     else:
#         mid = len(yacsu) // 2
#         x = yacsu[mid]
#         y = yacsu[mid]
#
#     return [x, y]