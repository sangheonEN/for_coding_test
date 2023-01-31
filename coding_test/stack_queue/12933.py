from collections import deque

# quack

def solution(s):




    save_queue = deque()
    s = deque(list(s))

    while s:
        save_queue.append(s.popleft())

        for i in s:
            if i == 'q':
                save_queue.append(s.popleft())




    # while s:




s = "quqacukqauackck"

solution(s)
