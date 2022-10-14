import copy


def dfs(start):
    # global result_list
    if len(result) == M:
        # result로 단순히 append하면 result pop하면 주소값이 같아져 result_list에 저장된 모든 원소가 똑같은 값으로 치환됨.
        # deepcopy(result) or result[:]로 하면 깊은복사로 새로운 result가 생성되어 저장됨으로 result에 pop이나 그런 처리를 되어 변경되어도 list원소가 치환되지 않음.
        # result_list.append(result[:])
        # result_list.append(copy.deepcopy(result))
        # print(result_list)
        print(" ".join(map(str, result)))
        return

    for i in range(start, len(input_list)):
        result.append(input_list[i])
        dfs(start)
        result.pop()

if __name__ == "__main__":
    # 이 문제에서 헤멘부분
    # 1. input_list 입력을 sort하지 않은 것
    # 2. result[:] 깊은 복사로 새롭게 객체를 생성해서 append해야함. 그래야 pop()이나 그런 처리로 인해 주소 값이 동일하게 치환되는 문제를 방지할 수 있음.

    N, M = map(int, input().split())
    # 한줄에 다 담음
    input_list = list(map(int, input().split()))

    # print(N, M)
    # print(input_list)

    input_list.sort()

    result_list = []
    result = []

    dfs(0)
    # print(result_list)
