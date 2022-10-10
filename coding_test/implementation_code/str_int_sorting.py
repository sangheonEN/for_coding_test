# CC1A2AB4B 가 들어오면 문자열을 오름차순으로 정렬하고, 각 숫자를 더한 값을 맨 뒤의 원소로 정렬한다.

# 문자열에서 int만 뽑아서 list로 변환
def extract_int_v(arr):
    return [int(v) for v in arr if not v.isalpha()]

# 문자열에서 str만 뽑아서 정렬
def extract_str_v(arr):
    return [v for v in arr if v.isalpha()]

arr1 = "K1KA5CB7"

# str에서 int만 뽑기
numbers = [int(v) for v in arr1 if not v.isalpha()]
print(numbers)
num = sum(numbers)

# str에서 알파벳만뽑기
# str_list = list(filter(extract_str_v, arr1))
str_list = [v for v in arr1 if v.isalpha()]
sort_str_list = sorted(str_list)
print(sort_str_list)

# list로 합치기
total_list = sort_str_list + [str(num)]
print(total_list)

# list원소 str로 합치기
final_str = ''.join(total_list)
print(final_str)

# 대신 sorted(s)처럼 쓰는 것은 가능하다. - 대신 return type은 list이다.
#
# 이를 하나로 이어진 문자열로 만들기 위해선 ''.join을 사용하면 된다.