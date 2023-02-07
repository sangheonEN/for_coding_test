"""
1차원 배열이 주어진다.
[2, 1, 3, 1, 2, 1]

- queue 자료구조를 통해 원소를 추가하고 원소를 삭제하는 순으로 처리가 진행된다. 단, 원소를 추가하는 것만 하거나 삭제하는 것만은 안됨 무조건 추가하고 삭제해야함.

- queue arr안에 1, 2, 3 원소의 카운트 수가 같아질때 까지 처리를 수행하고, 최단 횟수를 출력해라.

- 카운트 패키지 써야 히든 케이스 시간초과 되지 않음

"""
from collections import deque
from collections import Counter


# Counter 사용
if __name__ == "__main__":
    arr = [2, 1, 3, 1, 2, 1]

    arr = deque(arr)

    # cnt_dict[key] = value 여기서 key는 원소 1, 2, 3. value는 cnt 수
    cnt = 0

    while True:

        cnt_dict = Counter(arr)

        if cnt_dict[1] == cnt_dict[2] == cnt_dict[3]:
            break

        if cnt_dict[1] <= cnt_dict[2] or cnt_dict[1] <= cnt_dict[3]:
            arr.append(1)
            arr.popleft()
            cnt += 1
            print(arr)

        if cnt_dict[2] <= cnt_dict[1] or cnt_dict[2] <= cnt_dict[3]:
            arr.append(2)
            arr.popleft()
            cnt += 1
            print(arr)

        if cnt_dict[3] <= cnt_dict[1] or cnt_dict[3] <= cnt_dict[2]:
            arr.append(3)
            arr.popleft()
            cnt += 1
            print(arr)

    print(cnt)

# # deque.count 만 사용
# if __name__ == "__main__":
#
#     arr = [3, 3, 3, 2, 2, 2]
#
#     arr = deque(arr)
#
#     cnt = 0
#
#     while True:
#
#         if arr.count(1) == arr.count(2) == arr.count(3):
#             break
#
#         # 개별적으로 if문을 설계
#         # 원소 1에 대한 카운트를 검사할 때, 나머지 2, 3에 대한 것도 해줘야 순서 상관 없이 비교하는 것이된다!
#
#         if arr.count(1) <= arr.count(2) or arr.count(1) <= arr.count(3):
#             arr.append(1)
#             arr.popleft()
#             print(arr)
#             cnt += 1
#
#         if arr.count(2) <= arr.count(1) or arr.count(2) <= arr.count(3):
#             arr.append(2)
#             arr.popleft()
#             print(arr)
#             cnt += 1
#
#         if arr.count(3) <= arr.count(1) or arr.count(3) <= arr.count(2):
#             arr.append(3)
#             arr.popleft()
#             print(arr)
#             cnt += 1
#
#     print(cnt)
