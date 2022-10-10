# 첫 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
# 둘째 줄에 떡의 개별 높이가 주어진다.
# 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있습니다. 높이는 10억보다 작거나 같은 양의 정수 또는 0입니다.
# 출력: 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력!
# ex
# 4 6
# 19 15 10 17    -> 15
# 4 0 0 2 -> 6


def binary_search(target, array, start, end, knife_arr):
    middle = (start + end) // 2
    total = 0

    if start > end:
        return None

    for x in array:
        total += x - middle if (x - middle) >= 0 else 0

    if total > target:
        knife_arr.append(middle)

        return binary_search(target, array, middle+1, end, knife_arr)

    elif total < target:
        return binary_search(target, array, start, middle - 1, knife_arr)

    else:
        knife_arr.append(middle)
        return max(knife_arr)


N, M = list(map(int, input().split()))
array = list(map(int, input().split()))
array.sort()
knife = []
start = 0
end = max(array)

result = binary_search(M, array, start, end, knife)

print(result)


