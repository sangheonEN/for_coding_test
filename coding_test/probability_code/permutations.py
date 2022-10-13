def dfs(start):
    # 종료 조건
    if start == r:
        return result
    else:
        for i in range(len(n)):
            if check_list[i] == 0:
                result[start] = n[i]
                check_list[i] = 1
                dfs(start+1)
                check_list[i] = 0




if __name__ == "__main__":

    n = [1, 2, 3]
    r = 2

    result = [0] * r
    check_list = [0] * len(n)

    result2 = dfs(0)

    print(result2)