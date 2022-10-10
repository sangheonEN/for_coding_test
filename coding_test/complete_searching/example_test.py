# 인덱스 찾기

a = [1, 2, 3, 4, 5, 5]

b = a.index(max(a))
print(b)

# 중복 인덱스 찾기

rest_list = list(filter(lambda x: a[x] == 5, range(len(a))))

print(rest_list)


def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    one_score = 0
    two_score = 0
    three_score = 0

    for i, ans in enumerate(answers):
        i %= len(one)
        if one[i] == ans:
            one_score += 1
    for i, ans in enumerate(answers):
        i %= len(two)
        if two[i] == ans:
            two_score += 1
    for i, ans in enumerate(answers):
        i %= len(three)
        if three[i] == ans:
            three_score += 1

    scores = list()
    scores.append(one_score)
    scores.append(two_score)
    scores.append(three_score)

    # list내에 원하는 요소 값의 index를 중복하는 것까지 모두 뽑기!
    overlab_index = list(filter(lambda x: scores[x] == max(scores), range(len(scores))))

    print(overlab_index)

    for i in range(len(overlab_index)):
        overlab_index[i] += 1

    return overlab_index
