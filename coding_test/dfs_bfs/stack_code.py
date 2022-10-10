# stack
# input    5 2 3 4 pop 1 4 pop
# output   1 3 2 5

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(4)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()


# 스텍 출력
print(stack[::-1])
print(stack[:0:-1])
print(stack[:1:-1])
print(stack[:2:-1])
print(stack)
