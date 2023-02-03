# n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면, h의 최댓값이
# 120편 중 50번 이상 인용된 논문이 50펀 이상이고, 나머지 논문이 50번 이하 인용되었다면, h의 최댓값이 과학자의 H-Index


# h이상인걸 count해야된다!

def h_(citations, h):
    count_ = len(list(filter(lambda x: citations[x] >= h, range(len(citations)))))

    # print(count_)

    return count_


def solution(citations):
    n = len(citations)

    # result = 0
    # print(citations)

    citations.sort()
    result = 0

    for h in citations:

        if h >= h_(citations, h):

            result = h

            break

        else:
            if n <= h:
                return max(citations)

    return result