# python에서 스텍과 큐는 리스트 형태의 입력을 제약조건에 따라 위치를 뒤 바꾸면서 결과 값을 도출하는 문제이다.
from collections import deque

# deque를 통해서 popleft()함수를 구현하면 큐를 구현할 수 있다. 출력은 다시 list()형식으로 변환!
# a = [1, 2, 3, 4]
# a = deque(a)
# a.popleft()
# print(list(a))
# a.pop()
# print(list(a))

# append()함수를 통해서 맨 마지막 index에 원소를 넣어줌
# a.append(5)


# queue를 구현해보자 1, 2, 3, 4 원소가 차례대로 들어가고 1, 2, 3, 4가 차례대로 나오게!
# append와 popleft로 queue를 구현할 수 있다!
b = deque()
print("queue 구현!!")
for i in range(1, 5):
    b.append(i)
    print(b)

for _ in range(len(b)):
    b.popleft()
    print(b)

# stack을 구현해보자 1, 2, 3, 4 원소가 차례대로 들어가고 4, 3, 2, 1이 차례대로 나오게!
print("stack 구현!!")
for i in range(1, 5):
    b.append(i)
    print(b)

for _ in range(len(b)):
    b.pop()
    print(b)
