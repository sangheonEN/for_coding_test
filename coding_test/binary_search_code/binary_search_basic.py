a = [0, 2, 4, 6, 8, 10, 12, 14, 16]

# 이진 탐색은 내림차순으로 정렬된 array를 기반으로 탐색하는 방법!
# start, middle, end point 찾고
# target point의 값보다 middle point가 크면, middle point의 오른쪽 값들은 탐색할 필요 없기 때문에, end point를 middle point의 왼쪽으로 옮김
# target point의 값보다 middle point가 작으면, middle point의 왼쪽 값들은 탐색할 필요 없기 때문에, start point를 middle point의 오른쪽으로 옮김
# middle point가 target point와 같아 질때까지 반복

def binary_search_loop(target, array, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif target > array[mid]:
            start = mid + 1

        else:
            end = mid - 1
    return None


def binary_search_recursive(target, array, start, end):

    if start > end:
        return None

    middle_index = (start + end) // 2
    middle = array[middle_index]

    # middle = target
    if middle == target:
        return middle_index

    # target <= middle
    elif target < middle:
        end = middle_index - 1
        return binary_search_recursive(target, array, start, end)

    # target > middle
    # elif target > middle:
    else:
        start = middle_index + 1
        return binary_search_recursive(target, array, start, end)


# n = 원소의 개수, target = 내가 찾고자 하는 수 입력
n, target = list(map(int, input().split()))
# array = list 원소 전체 array
array = list(map(int, input().split()))

result = binary_search_recursive(target, array, 0, n-1)
print(result)

result2 = binary_search_loop(target, array, 0, n-1)
print(result2)
