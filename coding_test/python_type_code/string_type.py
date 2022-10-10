b = "aaAA aaa bb"

# print(b.join())
print(b.split(" "))
print(b.index("a",1, 3))
print(b.zfill(5))
# a를 b로 전체 다 바꾸기
print(b.replace("a", "b"))
# 앞에서부터 5개 까지만 replace
print(b.replace("a", "b", 5))

# 첫번째 문자열 대문자 변경
print(b.capitalize())
# 모든 문자열 소문자 변경
print(b.casefold())
# center(n, "문자열") n만큼의 문자열 길이를 출력하는데 "문자열" 앞뒤로 채움
print(b.center(100, "#"))
print(b.count("a"))
print(b.endswith("a"))
print(b.startswith("a"))
print(b.zfill(100))
print(b.find("a"))
# 알파벳 or 수일때 True
c = "!@#$"
print(c.isalnum())
print(b.isdecimal())
print(b.isdigit())
print(b.isalpha())
# 정수
T = "1234"
print(T.isnumeric())
#소문자
print(b.islower())
# 대문자
d = "AAA"
print(d.isupper())
# 문자열이 공백인지?
f = "  "
print(f.isspace())

print(len(d))
