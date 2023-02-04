# 최대 K번 바꿔칠 수 있다.
# 두 A, B 배열의 원소를 최대 K번 바꿔서 배열 A의 원소의 합이 최대가 되는 최대 값을 출력하시오.
#%%
K = 3
a_arr = [1, 2, 5, 4, 3]
b_arr = [5, 5, 6, 6, 5]


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]
    # pivot은 가장 앞에 수로 정하고, 나머지 tail list를 [1:] 인덱싱하여서 얻는다.
    print(tail)

    # pivot value 기준 왼쪽 영역 arr은 pivot value 보다 작은 arr가 되고
    # pivot value 기준 오른쪽 영역은 pivot value 보다 큰 arr가 된다.
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(a_arr))

#%%
K = 3
a_arr = [1, 2, 5, 4, 3]
b_arr = [5, 5, 6, 6, 5]

def solution(A, B, change_num):

    if (len(A) <= 1 and len(B) <= 1):
        return sum(A)

    A.sort()
    B.sort(reverse=True)

    for i in range(change_num):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break

    max_value = sum(A)

    return max_value, A, B

print(solution(a_arr, b_arr, K))