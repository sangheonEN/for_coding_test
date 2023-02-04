# pivot value이 설정되고
# 왼쪽에서부터는 pivot value보다 큰 값을 선택할때까지 방문
# 오른쪽에서부터는 pivot value보다 작은 값을 선택할때까지 방문
# 두 값이 정해지면, 두 위치를 switching
# 왼쪽에서부터 선택된 큰 값이 오른쪽에서부터 선택된 작은 값 위치와 엇갈리면, 작은 값과 pivot value를 switching
# 그러면 pivot value의 왼쪽 영역은 pivot value 보다 작은 arr가 되고
# pivot value의 오른쪽 영역은 pivot value 보다 큰 arr가 된다.
# 이때 두 arr에 대해 다시 재귀적으로 퀵 정렬 반복
# 이러한 과정을 재귀적으로 수행하도록 만듬
# O(Nlog_2N) 시간복잡도를 기대할 수 있다.


def quick_sort(arr):

    # array의 원소가 하나 이하일 경우
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))


#%%
# pivot value이 설정되고
# 왼쪽에서부터는 pivot value보다 큰 값을 선택할때까지 방문
# 오른쪽에서부터는 pivot value보다 작은 값을 선택할때까지 방문
# 두 값이 정해지면, 두 위치를 switching
# 왼쪽에서부터 선택된 큰 값이 오른쪽에서부터 선택된 작은 값 위치와 엇갈리면, 작은 값과 pivot value를 switching
# 그러면 pivot value의 왼쪽 영역은 pivot value 보다 작은 arr가 되고
# pivot value의 오른쪽 영역은 pivot value 보다 큰 arr가 된다.
# 이때 두 arr에 대해 다시 재귀적으로 퀵 정렬 반복

def quick_sort2(arr, start, end):

    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    # 엇갈릴때 탈출
    while (left <= right):
        # 피벗보다 큰 데이터 찾을때까지 왼쪽에서 오른쪽으로 탐색
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터 찾을때까지 오른쪽에서 왼쪽으로 탐색
        while (right > start and arr[right] > arr[pivot]):
            right -= 1

        # 엇갈린다면, 작은 데이터(arr[right]!)와 피벗을 교체
        if (left > right):
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않는다면, 작은 데이터와 큰 데이터를 교체
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # 분할하고, 왼쪽 arr와 오른쪽 arr를 나눠서 다시 재귀적으로 정렬 수행
    quick_sort2(arr, start, right -1)
    quick_sort2(arr, right+1, end)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

print(array)
quick_sort2(array, 0, len(array)-1)
print(array)