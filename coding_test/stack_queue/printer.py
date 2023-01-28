"""
중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

# 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return

"""

from collections import deque

def solution(priorities, location):
    p = deque(priorities)
    temp = deque([x for x in range(len(p))])
    order = 0

    while p:
        first = p.popleft()
        if p:
            if first < max(p):
                # max보다 작으면 뒤로 넣기! temp, priorities 둘다!
                temp.append(temp.popleft())
                p.append(first)
            else:
                order += 1
                if temp[0] == location:
                    return order
                else:
                    temp.popleft()

    return order + 1


priorities = [1, 2, 3, 4, 0]
location = 4
print(solution(priorities, location))