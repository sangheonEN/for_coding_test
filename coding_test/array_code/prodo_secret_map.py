# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# 비트연산 AND : &, OR : |, XOR : ^, NOT : ~

# a = bin(9)
# b = bin(30)
# c = bin(9 | 30)
# print(a)
# print(b)
# print(c)
#
# d = str(a)[2:].replace("1", "#").replace("0", ' ')
# e = str(b)[2:].replace("1", "#").replace("0", ' ')
# f = str(c)[2:].replace("1", "#").replace("0", ' ')
# print(d)
# print(e)
# print(f)

# # 두 arr에 속한 요소를 bit 연산하여 "#", " "로 변환
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
#
# list_1 = list(zip(arr1, arr2))
# print(list_1)
#
# for i in list_1:
#     print(i)
#     k = bin(i[0] | i[1])
#     print(k)
#     g = str(k)[2:].replace("1", "#").replace("0", " ")
#     print(g)

# 자리수 고려하기 zfill(n) n = 자리수. zfill은 n의 자리수 만큼 데이터 앞에 0을 삽입 넣음.
n = 5

arr1 = [3, 9, 20, 28, 18, 11]
arr2 = [5, 30, 1, 21, 17, 28]

list_1 = list(zip(arr1, arr2))
print(list_1)

for i in list_1:
    # print(i)
    k = bin(i[0] | i[1])[2:].zfill(n)
    print(k)
    # f = bin(i[0] | i[1])[2:]
    # print(f)
    g = str(k).replace("1", "#").replace("0", " ")
    print(g)




