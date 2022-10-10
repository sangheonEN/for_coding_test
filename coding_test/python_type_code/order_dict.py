from collections import OrderedDict

# OrderedDict()는 기존의 dict와 달리 저장된 순서가 상관이 있어, 저장되는 순서까지 비교대상으로 적용된다! 그래서 조건문에서 활용할때 순서까지 맞아야 True가 반환됨.
c = OrderedDict()
c['a'] = 100
c['b'] = 200
# popitem(last) 데이터반환삭제 last = False -> Queue 자료구조 처럼 맨 처음 삽입된 데이터를 반환하고 삭제, True -> Stack 자료구조 처럼 맨 마지막에 삽입된 데이터를 반환, 삭제
# c.popitem(last = False)
c.popitem(last = True)

# update({key:value}): dict 원소 추가!
c.update({"g":1000})
print(c)

# move_to_end(key, last): key값에 해당되는 아이템을 OrderedDict의 맨 뒤 혹은 맨 앞으로 이동시키는 함수이다. last = True면, 아이템이 맨 뒤로 이동. False면, 맨 앞으로 이동
c.move_to_end("a")
print(c)

# dict 활용해서 문자열의 특정 원소를 key값 기준으로 저장하고, key 값의 item을 popitem으로 반환하거나 삭제 시켜보자!
# 또한 "."은 block을 나타내고 block을 기준으로 각기 다른 명령어가 저장된다. 근데 block이 사라지고 생성된다. .수가 많아지면 생성 적어지면 적어진 수만큼에 생성된 block이 삭제 그러면 그 명령어도 삭제
# input: [". a=3", "... print a", "..... b=4", "print b"]
# output: a=3, b=4
dict_1 = OrderedDict()

list_1 = list(map(str, input().split(", ")))
print(list_1)

dict_1[".a"] = 1
dict_1["a"] = 2
dict_1["b"] = 3
dict_1["b"] = 4
dict_1["c"] = 5
dict_1["c"] = 6

# "c" 원소 추가
dict_1.update({"c":7})

# "a" 중 마지막 원소 반환 후 삭제
print(dict_1.items())
print(dict_1)


