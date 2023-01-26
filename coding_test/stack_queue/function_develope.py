import math
from collections import deque

# 1. 각 기능은 진도 100% 일때 서비스 반영
# 2. 뒤에 있는 기능이 먼저 개발될 수 있음. 이러한 경우 앞에 있는 기능이 배포될때 같이 배포
# 3. 배포 순서 progresses, 개발 속도 speeds 입력될때
# 4. 각 배포마다 몇 개의 기능이 배포되는지 return
# 작업의 개수 progresses, speeds 배열 길이 <= 100
# 작업 진도 100미만 자연수. 작업 속도 100 이하 자연수
# 배포는 하루에 한번 가능

# 첨에 내가 푼 코드 완전 하드코딩했다.. 노답이다..
# 심기일전으로 다시 재도전해보자.

# def solution(progresses, speeds):
#     complete_time_arr = []
#     employ_arr = []
#     for progress, speed in zip(progresses, speeds):
#         print(progress, speed)
#         complete_time = math.ceil((100 - progress) / speed)
#         complete_time_arr.append(complete_time)

#     print(complete_time_arr)
#     cnt = 0
#     # 앞에꺼가 뒤어꺼보다 크면 pop
#     complete_time_arr = deque(complete_time_arr)

#     while True:
#         if not complete_time_arr:
#             break

#         if len(complete_time_arr) == 1:
#             cnt += 1
#             employ_arr.append(cnt)
#             break

#         if complete_time_arr[0] <= complete_time_arr[1]:
#             cnt += 1
#             employ_arr.append(cnt)
#             complete_time_arr.popleft()
#             cnt = 0
#         elif complete_time_arr[0] > complete_time_arr[1]:
#             cnt += 1
#             complete_time_arr.popleft()

#     return employ_arr


# pro = [93, 30, 55]
# speeds = [1, 30, 5]

# pop(index) -> pop(0)으로 하면 popleft()와 같음
# pro.pop(0)
# print(pro)


# 두 번째 풀이
# progresses와 speeds의 관계를 잘 살펴보고 배포 날마다 cnt를 해주자!

def solution(progresses, speeds):

    result = []
    time = 0
    cnt = 0

    while len(progresses) > 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                result.append(cnt)
                cnt = 0
            time += 1

    result.append(cnt)
    return result


print(solution(pro, speeds))
