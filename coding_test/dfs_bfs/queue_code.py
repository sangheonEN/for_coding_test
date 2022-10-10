# queue
# input    5 2 3 4 pop 1 4 pop
# output   3 4 1 4
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

# queue 출력
print(queue)
queue.reverse()
print(queue)